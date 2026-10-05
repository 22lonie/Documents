#!/usr/bin/env python
# coding: utf-8

# ##Dijkstra's algorithim procedure  
# ##Input data of town's departure and destination and distances 
# ##Town's departure is at choice point(Kegati town) 
# ##The system finds the possible routes to be passed based on existing choice points and their closest relationships 
# ##The systems find the possible routes with the lowest value(distance) 
# ##If the route obtained by the town which is not a choice point, then the town is added to the choice point. 
# ##The programe repeats the steps above until a route is found 
# 

# In[12]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# === Step 1: Input Data (Town Connections) ===
data = {
    'from_vertex': [
        'KEGATI','BOBARACHO','DARAJA MBILI','DENMARK','KISII MIGORI JUNCTION','NYAMATARO',
        'NYAKOE','KEGATI','ITUMBE', 'MENYINKWA', 'NYAMOKENYE', 'SUNEKA', 'RIANA',
        'BOBARACHO','KISII MIGORI JUNCTION','GESONSO', 'KISII MIGORI JUNCTION',
        'DENMARK', 'NYATIEKO'
    ],
    'to_vertex': [
        'BOBARACHO','DARAJA MBILI','DENMARK','KISII MIGORI JUNCTION','NYAMATARO','NYAKOE',
        'MOSOCHO','ITUMBE','MENYINKWA', 'NYAMOKENYE', 'SUNEKA', 'RIANA','NYAMATARO',
        'MENYINKWA','GESONSO', 'NYAMOKENYE','SUNEKA','NYATIEKO', 'NYAKOE'
    ],
    'distance': [
        5.3,5.4,2.1,3.4,6.1,2.9,11.1,7.6,22.6,9.8,5,7.4,12,5.7,1.8,0.7,6.5,4.1,7.4
    ]
}

df = pd.DataFrame(data)

# === Step 2: Create Weighted Graph ===
G = nx.Graph()
for i, row in df.iterrows():
    G.add_edge(row['from_vertex'], row['to_vertex'], weight=row['distance'])

# === Step 3: Draw Graph (Safe version with no error) ===
fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=3)
nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
ax.set_title("Town Network")
plt.show()

# === Step 4: Dijkstra's Algorithm ===
start = 'KEGATI'
end = 'MOSOCHO'
try:
    shortest_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    shortest_distance = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
    print(f"\nDijkstra: Shortest path from {start} to {end}: {shortest_path}")
    print(f"Distance: {shortest_distance:.2f} km")
except nx.NetworkXNoPath:
    print(f"\nNo path found between {start} and {end}")

# === Step 5: Floyd-Warshall All-Pairs Shortest Distances ===
all_pairs = dict(nx.floyd_warshall(G, weight='weight'))
print(f"\nFloyd-Warshall: Distance from KEGATI to RIANA: {all_pairs['KEGATI']['RIANA']:.2f} km")

# ==


#  Nairobi County Locations
# Let’s define a few key locations in Nairobi County (these can be streets, districts, or landmarks) and the distances between them.
# 
# Locations:
# Nairobi Central Business District (CBD)
# Westlands
# Kenyatta National Hospital (KNH)
# Nairobi Railway Station
# Jomo Kenyatta International Airport (JKIA)
# Karen
# Gikambura
# Lang'ata
# Eastleigh
# Distances (in km):
# CBD ↔ Westlands = 5
# CBD ↔ KNH = 3
# CBD ↔ Nairobi Railway Station = 2
# CBD ↔ JKIA = 15
# Westlands ↔ Karen = 18
# KNH ↔ Gikambura = 25
# Nairobi Railway Station ↔ Lang'ata = 10
# Lang'ata ↔ JKIA = 5
# Eastleigh ↔ CBD = 7

# In[13]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# === Step 1: Input Data (Nairobi Locations) ===
data = {
    'from_vertex': [
        'CBD', 'CBD', 'CBD', 'CBD', 'Westlands', 'Westlands', 'KNH', 'KNH', 
        'Nairobi Railway Station', 'Nairobi Railway Station', 'Lang\'ata', 
        'Lang\'ata', 'Karen', 'Gikambura', 'Eastleigh'
    ],
    'to_vertex': [
        'Westlands', 'KNH', 'Nairobi Railway Station', 'JKIA', 'Karen', 'KNH', 'Gikambura', 
        'Nairobi Railway Station', 'Lang\'ata', 'Eastleigh', 'JKIA', 'Karen', 'Westlands', 'Gikambura', 'CBD'
    ],
    'distance': [
        5, 3, 2, 15, 18, 25, 25, 10, 5, 7, 5, 18, 18, 25, 7
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# === Step 2: Create Weighted Graph ===
G = nx.Graph()
for i, row in df.iterrows():
    G.add_edge(row['from_vertex'], row['to_vertex'], weight=row['distance'])

# === Step 3: Draw Graph (Safe version with no error) ===
fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=3)
nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
ax.set_title("Nairobi County Road Network")
plt.show()

# === Step 4: Dijkstra's Algorithm (Example: CBD to JKIA) ===
start = 'CBD'
end = 'JKIA'
try:
    shortest_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    shortest_distance = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
    print(f"\nDijkstra: Shortest path from {start} to {end}: {shortest_path}")
    print(f"Distance: {shortest_distance:.2f} km")
except nx.NetworkXNoPath:
    print(f"\nNo path found between {start} and {end}")

# === Step 5: Floyd-Warshall All-Pairs Shortest Distances ===
all_pairs = dict(nx.floyd_warshall(G, weight='weight'))
print(f"\nFloyd-Warshall: Distance from CBD to Karen: {all_pairs['CBD']['Karen']:.2f} km")

# === Step 6: Print All-Pairs Distance Matrix ===
nodes = list(G.nodes())
distance_matrix = pd.DataFrame(index=nodes, columns=nodes)

for u in nodes:
    for v in nodes:
        distance_matrix.loc[u, v] = round(all_pairs[u][v], 2)

print("\nAll-Pairs Distance Matrix:")
print(distance_matrix)

