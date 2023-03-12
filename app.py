
# pip install simple-image-download==0.4

from simple_image_download import simple_image_download as simp
 
response = simp.simple_image_download()

response.download("Bangladesh Flags", limit=100, extensions=[".jpg", ".png", ".jpeg"])
 