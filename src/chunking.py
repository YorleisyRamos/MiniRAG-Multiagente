def dividir_en_chunks(texto, tamaño=500):
    chunks = []
    palabras = texto.split()
    chunk = []
    longitud = 0

    for palabra in palabras:
        chunk.append(palabra)
        longitud += len(palabra) + 1  # +1 por el espacio
        if longitud >= tamaño:
            chunks.append(" ".join(chunk))
            chunk = []
            longitud = 0

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

