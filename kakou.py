from PIL import Image, ImageChops
import os # ファイルやフォルダ操作
import glob
import shutil
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
  im_original = Image.open(os.path.join(dir_name, file))
  name, ext = os.path.splitext(os.path.basename(file))
  width, height = im_original.size

  if height > width: # 縦長
    im = crop_center(im_original, 750, 1050)
  else:
    # im = crop_center(im_original, 1100, 750)
    im = im_original

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

  print(str(i) + " done!")
  i += 1

# 終了時に元の画像を削除
shutil.rmtree(dir_name)
os.mkdir(dir_name)

print("Complete!")