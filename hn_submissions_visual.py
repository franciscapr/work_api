from operator import itemgetter
import requests
import plotly.express as px

# Hace una llamada a la API y verifica la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Procesa información sobre cada envío
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    try:
        response_dict = r.json()
        title = response_dict.get('title', 'No title')
        comments = response_dict.get('descendants', 0)
        
        # Saltar posts sin título o comentarios inválidos
        if not title or comments is None:
            continue

        submission_dicts.append({
            'title': title,
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': comments
        })

    except KeyError:
        print(f"Post {submission_id} omitido por error de clave.")

# Ordenar por número de comentarios de mayor a menor
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extraer datos para graficar
titles = [f"<a href='{sub['hn_link']}'>{sub['title']}</a>" for sub in submission_dicts]
comments = [sub['comments'] for sub in submission_dicts]

# Crear visualización con Plotly
fig = px.bar(
    x=titles,
    y=comments,
    labels={'x': 'Envío', 'y': 'Número de Comentarios'},
    title="Discusiones más activas en Hacker News"
)

# Mejorar apariencia
fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    xaxis_tickangle=-45
)

fig.update_traces(marker_color='pink', marker_opacity=0.7)

fig.show()
