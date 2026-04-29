def generate_response(query, results):
    response = f"Based on your mood: '{query}', here are my top anime picks:\n\n"

    for i, row in enumerate(results.itertuples(), 1):
        response += (
            f"{i}. {row.name}\n"
            f"Genre: {row.genre}\n"
            f"Type: {row.type}\n"
            f"Rating: {row.rating}\n\n"
        )

    return response
