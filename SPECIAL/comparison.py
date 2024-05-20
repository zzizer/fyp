import numpy as np
import face_recognition

def comparison(charactertics1, charactertics2):
    matching_count = sum(x==y for x, y in zip(charactertics1, charactertics2))

    if len(charactertics1) > len(charactertics2):
        total_elements = len(charactertics2)
    else:
        total_elements = len(charactertics1)

    percentage_on_matching = (matching_count / total_elements) * 100

    print(f"Matching Percentage: {percentage_on_matching}")

    return percentage_on_matching


def face_encoding_similarity(scanned_face_encoding, saved_face_encoding):
    byte_string_content = saved_face_encoding[2:-1]

    saved_face_encoding = byte_string_content.encode('latin1').decode('unicode_escape').encode('latin1')
    # print(type(scanned_face_encoding))
    # print(type(saved_face_encoding))
    scanned_face_encoding = np.frombuffer(scanned_face_encoding, dtype=np.float64)
    saved_face_encoding = np.frombuffer(saved_face_encoding, dtype=np.float64)
    print('this step')
    face_distances = face_recognition.face_distance([scanned_face_encoding], saved_face_encoding)
    print('this step again')
    similarity_percentage = (1 - face_distances[0]) * 100
    print(f'Similarity Percentage: {similarity_percentage}')

    return similarity_percentage