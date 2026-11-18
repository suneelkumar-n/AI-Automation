import pymupdf
import sys
doc = pymupdf.open("samples/2627-GW02-101-GA01.pdf")
page = doc[0]
#for x0,y0,x1,yx,text,*_ in page.get_text("words"):
 #   print(f"{x0:7.1f} {y0:7.1f}  {text}")

r = page.rect
corner = pymupdf.Rect(r.width * 0.6, r.height * 0.75, r.width, r.height)  # bottom-right

words = page.get_text("words", clip=corner)
lines = [d for d in page.get_drawings() if d["rect"].intersects(corner)]
print("words in title block:", len(words))
print("vector shapes in title block:", len(lines))