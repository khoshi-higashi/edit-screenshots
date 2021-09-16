from PIL import Image, ImageChops
import os # ファイルやフォルダ操作
import glob
dir_name = "mikakou" # 画像が入っているフォルダ
new_dir_name = "new" # 画像を保存する先のフォルダ

def crop_center(pil_img, crop_width, crop_height): # 画像の中心を切り出し
  img_width, img_height = pil_img.size
  return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))

# ディレクトリが存在しない場合は作成する
if not os.path.exists(new_dir_name):
  os.mkdir(new_dir_name)

files = os.listdir(dir_name)

i = 1

for file in files: # ホーム画面用の処理
  im = Image.open(os.path.join(dir_name, file))
  name, ext = os.path.splitext(os.path.basename(file))
  width, height = im.size

  if height > width: # 縦長
    im = crop_center(im, 750, 1050)
  else:
    im = crop_center(im, 1050, 750)

  # 背景色画像を生成
  im2 = im.convert("RGB")
  bg = Image.new("RGB", im2.size, im2.getpixel((0, 0)))

  # 背景色画像と元画像の差分画像を生成
  diff = ImageChops.difference(im2, bg)

  # 背景との境界を求めて画像を切り抜く
  croprange = diff.convert("RGB").getbbox()
  nim = im.crop(croprange)

  # 切り抜いた画像を保存
  nim.save(os.path.join(new_dir_name, '%s.png' % name))
  # nim.save(os.path.join(new_dir_name, file))
  print(str(i) + " done!")
  i += 1
print("Complete!")