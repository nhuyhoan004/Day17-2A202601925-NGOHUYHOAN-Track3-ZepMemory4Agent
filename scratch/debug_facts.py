import json
from src.zep_common import get_zep_client, render_graph_search

client = get_zep_client()

print("--- Edges for G16 ---")
res = client.graph.search(user_id="minh-lab17", query="open loop", scope="edges", limit=20)
print(render_graph_search(res))

print("--- Edges for G17 ---")
res = client.graph.search(user_id="minh-lab17", query="timeline coroutine", scope="edges", limit=20)
print(render_graph_search(res))

print("--- Nodes for G16 ---")
res = client.graph.search(user_id="minh-lab17", query="open loop", scope="nodes", limit=20)
print(render_graph_search(res))
