from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # ------------------------------------------------------------------
    # TODO 1/4 — Long-term: Context Block + fact edges
    # ------------------------------------------------------------------
    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # 1) Prime the evaluation thread so Zep knows the current query context
        prime_eval_thread(self.client, user_id, thread_id, query)

        # 2) Retrieve the Context Block that Zep assembled for this user/thread
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        # 3) Bonus: append fact edges with validity ranges for recency/conflict
        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        return join_nonempty([context_block, fact_text], sep="\n\n")

    # ------------------------------------------------------------------
    # TODO 2/4 — Episodic: user graph episode search
    # ------------------------------------------------------------------
    def retrieve_episodic(self, user_id: str, query: str) -> str:
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=5,
        )
        # Cap each episode to keep more distinct results within budget
        return render_graph_search(results, episode_char_cap=180)

    # ------------------------------------------------------------------
    # TODO 3/4 — Semantic: standalone knowledge graph search
    # ------------------------------------------------------------------
    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        q = cap_query(query)
        # scope="episodes" preserves literal markers (e.g. PAYMENT-RULE-3)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            # Fallback to nodes if episodes scope is unsupported
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )
        return render_graph_search(results)

    # ------------------------------------------------------------------
    # TODO 4/4 — Assemble context with 10/4/3/3 token budget
    # ------------------------------------------------------------------
    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # ContextBudgetManager trims each layer to its budget (STM 10%, LTM 4%,
        # EPI 3%, SEM 3%) in priority order and returns merged text + breakdown.
        return self.budget.assemble(layers)
