def comparison(charactertics1, charactertics2):
    matching_count = sum(x==y for x, y in zip(charactertics1, charactertics2))

    if len(charactertics1) > len(charactertics2):
        total_elements = len(charactertics2)
    else:
        total_elements = len(charactertics1)

    percentage_on_matching = (matching_count / total_elements) * 100

    # print(f"Matching Percentage: {percentage_on_matching}")

    return percentage_on_matching


def face_encoding_similarity(scanned_face_encoding, saved_face_encoding):
    scanned_face_encoding = np.frombuffer(scanned_face_encoding, dtype=np.float64)
    saved_face_encoding = np.frombuffer(saved_face_encoding, dtype=np.float64)

    face_distances = face_recognition.face_distance([scanned_face_encoding], saved_face_encoding)

    similarity_percentage = (1 - face_distances[0]) * 100

    return percentage_on_matching