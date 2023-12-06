
# This is the input
face = input()


substring1 = ":)"
substring2 = ":("

# I'm going to use the method replace in order to replace the substrings
if substring1 in face:
     face_new = face.replace(substring1, "🙂")
if substring2 in face:
     face_new = face.replace(substring2, "🙁")
if substring1 in face and  substring2 in face:
     face_new = face.replace(substring1, "🙂").replace(substring2, "🙁")




print(face_new)
