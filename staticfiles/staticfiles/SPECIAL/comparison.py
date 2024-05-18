def comparison(charactertics1, charactertics2):
    matching_count = sum(x==y for x, y in zip(charactertics1, charactertics2))

    if len(charactertics1) > len(charactertics2):
        total_elements = len(charactertics2)
    else:
        total_elements = len(charactertics1)

    percentage_on_matching = (matching_count / total_elements) * 100

    # print(f"Matching Percentage: {percentage_on_matching}")

    return percentage_on_matching

# def comparision(charactertics1, charactertics2):
#     print(f"Comparing: {charactertics1} and {charactertics2}")

#     matching_count = sum(x == y for x, y in zip(charactertics1, charactertics2))

#     print(f"Matching Count: {matching_count}")

#     if len(charactertics1) > len(charactertics2):
#         total_elements = len(charactertics2)
#     else:
#         total_elements = len(charactertics1)

#     print(f"Total Elements: {total_elements}")

#     percentage_on_matching = (matching_count / total_elements) * 100

#     print(f"Matching Percentage: {percentage_on_matching}")

#     return percentage_on_matching

# comparision([3, 3, 95, 31, 0, 1, 32, 1, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 6, 0, 115, 0, 15, 0, 204, 207, 255, 243, 63, 63, 255, 51, 238, 174, 170, 170, 170, 170, 170, 166, 85, 85, 85, 85, 85, 81, 16, 68, 64, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 147, 44, 254, 24, 20, 67, 222, 55, 25, 108, 190, 77, 155, 40, 126, 47, 161, 25, 126, 42, 166, 216, 190, 82, 40, 150, 222, 91, 44, 106, 30, 97, 177, 235, 190, 68, 178, 216, 190, 78, 53, 192, 30, 98, 183, 150, 126, 69, 61, 129, 126, 66, 67, 3, 62, 20, 157, 194, 255, 68, 163, 236, 95, 33, 41, 89, 159, 70, 43, 44, 191, 101, 64, 151, 63, 18, 64, 195, 223, 36, 65, 153, 159, 50, 170, 129, 220, 70, 184, 88, 124, 44, 45, 194, 125, 90, 63, 0, 61, 39, 180, 25, 154, 37, 186, 23, 59, 32, 58, 192, 155, 92, 193, 193, 27, 39, 49, 194, 185, 25, 36, 66, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 3, 99, 20, 0, 1, 32, 1, 133, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 7, 0, 119, 0, 0, 0, 0, 0, 0, 3, 192, 51, 243, 255, 255, 255, 239, 251, 238, 186, 170, 170, 170, 170, 170, 169, 149, 85, 85, 85, 85, 85, 84, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 18, 105, 158, 43, 151, 89, 158, 23, 159, 218, 62, 45, 33, 66, 62, 40, 37, 194, 222, 92, 171, 234, 222, 87, 175, 86, 94, 62, 181, 129, 190, 105, 182, 42, 254, 76, 189, 128, 254, 37, 67, 67, 30, 16, 147, 131, 95, 19, 26, 2, 223, 38, 156, 153, 63, 65, 33, 192, 159, 110, 48, 41, 127, 11, 53, 196, 63, 64, 42, 153, 28, 70, 45, 64, 188, 64, 48, 24, 220, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 95, 31, 0, 1, 32, 1, 122, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 6, 0, 115, 0, 15, 0, 204, 207, 255, 243, 63, 63, 255, 51, 238, 174, 170, 170, 170, 170, 170, 166, 85, 85, 85, 85, 85, 81, 16, 68, 64, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 147, 44, 254, 24, 20, 67, 222, 55, 25, 108, 190, 77, 155, 40, 126, 47, 161, 25, 126, 42, 166, 216, 190, 82, 40, 150, 222, 91, 44, 106, 30, 97, 177, 235, 190, 68, 178, 216, 190, 78, 53, 192, 30, 98, 183, 150, 126, 69, 61, 129, 126, 66, 67, 3, 62, 20, 157, 194, 255, 68, 163, 236, 95, 33, 41, 89, 159, 70, 43, 44, 191, 101, 64, 151, 63, 18, 64, 195, 223, 36, 65, 153, 159, 50, 170, 129, 220, 70, 184, 88, 124, 44, 45, 194, 125, 90, 63, 0, 61, 39, 180, 25, 154, 37, 186, 23, 59, 32, 58, 192, 155, 92, 193, 193, 27, 39, 49, 194, 185, 25, 36, 66, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])