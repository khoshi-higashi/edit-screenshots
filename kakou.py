from PIL import Image
import os # ファイルやフォルダ操作
dir_name = "mikakou" # 画像が入っているフォルダ
new_dir_name = "new" # 画像を保存する先のフォルダ

def crop_center(pil_img, crop_width, crop_height): # 画像の中心を切り出し
  img_width, img_height = pil_img.size
  return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))

files = os.listdir(dir_name)

i = 1

for file in files: # ホーム画面用の処理
  im = Image.open(os.path.join(dir_name, file))
  width, height = im.size
  if width > height: # 横長
    im_new = crop_center(im, 1000, 750)
  else:
    im_new = crop_center(im, 750, 1000)
  im_new.save(os.path.join(new_dir_name, file))
  print(str(i) + " done!")
  i += 1

print("Complete!")