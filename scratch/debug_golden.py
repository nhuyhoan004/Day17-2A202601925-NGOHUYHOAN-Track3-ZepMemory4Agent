import json
from src.zep_common import get_zep_client, render_graph_search
from src.utils import cap_query

client = get_zep_client()

# Check G16
q16 = "Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh thuc trong lab."
print("--- G16 Episodes ---")
res16 = client.graph.search(user_id="minh-lab17", query=cap_query(q16), scope="episodes", limit=10)
print(render_graph_search(res16, episode_char_cap=200))

# Check G18
q18 = "Viet slide hau kiem: root cause async lan truoc la gi, va khi cat context cho agent thi ty le budget bon tang nho trong lab la bao nhieu? Can reflection that va ma ngan sach, khong doan."
print("--- G18 Semantic ---")
res18 = client.graph.search(graph_id="vinuni-lab17-domain-kb", query=cap_query(q18), scope="episodes", limit=10)
print(render_graph_search(res18))

