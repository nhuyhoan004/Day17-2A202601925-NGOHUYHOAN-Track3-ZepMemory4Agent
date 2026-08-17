# README Submission — Lab 17

**Họ tên:** Ngô Huy Hoàn  
**MSSV:** 2A202601925  
**Track:** 3 — Zep Memory for Agent

---

## 1. Layer quan trọng nhất trong bộ test

**Long-term memory** là layer quan trọng nhất, chiếm 4/11 case (E02, E03, E08, E09) tương đương 20/56 điểm tự động. Long-term quyết định khả năng cross-session recall: preference ngôn ngữ (E02), open-loop/deadline (E03), recency khi conflict xảy ra giữa Python→TypeScript cho BLUEBIRD-42 (E08), và user isolation giữa minh-lab17/lan-lab17 (E09). Nếu `retrieve_long_term` sai, toàn bộ 4 case FAIL và mất 20 điểm.

## 2. Trade-off Context Block / Zep vs Redis + Qdrant

**Zep Cloud** cung cấp managed memory pipeline: tự động extract facts, xây knowledge graph, xử lý recency/conflict, và trả Context Block đã assemble sẵn — chỉ cần 2-3 dòng code (`prime_eval_thread` → `get_user_context`). **Redis + Qdrant** yêu cầu tự thiết kế schema, embedding pipeline, conflict resolution, và garbage collection. Zep nhanh hơn để prototype nhưng phụ thuộc cloud, có latency network (trung bình ~1-2s cho long-term), và chi phí theo usage. Redis+Qdrant cho full control, latency thấp hơn (local), nhưng engineering cost cao và phải tự implement recency logic.

## 3. Guardrail chống memory poisoning

Lab dùng 3 guardrail: (1) **Consent gate** (`data/consent.json` + `require_memory_consent`) — chỉ ingest khi user opt-in `memory_opt_in=true`; (2) **PII minimization** (`minimize_pii` trong `privacy_guard.py`) — redact email/phone trước khi lưu vào durable memory; (3) **User-scoped namespace** — mỗi user có `user_id` riêng, long-term/episodic search luôn filter theo `user_id`, tránh data leak giữa users (E09 verify điều này). Heartbeat cũng bị giới hạn: chỉ de-duplicate/recap, không được tự thêm instruction mới vào memory.

---

## 4. Phân tích benchmark

1. **Layer hit rate thấp nhất:** Tất cả layer đều đạt 100% (11/11 PASS). Trong baseline no-memory, long-term/episodic/semantic đều 0% — chỉ short-term (E01, E10) pass vì evidence nằm trong current thread.

2. **Query retrieve nhiều token nhất:** E03 (long_term, 1436 tokens) và E08 (long_term, 1432 tokens) retrieve nhiều token nhất vì Context Block chứa đầy đủ user summary + episodes + fact edges.

3. **E07 (mixed):** Cần kết hợp **long-term** (Python preference cho ORCHID-27) + **semantic** (Idempotency-Key từ payment retry policy). Evidence bắt buộc: `Python` và `Idempotency-Key`.

4. **Token reduction:** Memory-enabled có token reduction trung bình 20.2%, no-memory đạt 81.8%. Nhưng no-memory chỉ PASS 2/11 — reduction cao vì không retrieve gì cả. Token reduction chỉ có ý nghĩa khi đi kèm hit rate cao.

## 5. Recency (E08) và Compaction (E10)

**E08:** Minh ban đầu prefer Python (session 1), sau đó đổi sang TypeScript+NestJS cho BLUEBIRD-42 (session 2). Zep xử lý conflict bằng recency — fact mới (`TypeScript`) override fact cũ, fact cũ vẫn giữ trong graph với `invalid_at` để audit.

**E10:** Compaction giữ `REVIEW-DEADLINE-1600` nhờ durable note extraction. Dù raw turns bị evict (sliding window giữ 6 turns gần nhất), constraint quan trọng được promote thành durable note và luôn render ở đầu context. Buffer strategy không đủ vì token tăng tuyến tính khi conversation dài.
