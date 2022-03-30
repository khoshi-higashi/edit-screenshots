# edit-screenshots

スマートフォンでスクリーンショットを行った際の画面上部のステータスバーや余白を削除します。

Removes the status bar and margins at the top of the screen when screenshots are taken on a smartphone.

## 使い方

- レポジトリをcloneする。Clone the repository.
- 加工したい画像と`main.py`を同じ場所に置く。Put the image you want to process and `main.py` in the same place.
- `main.py`を実行する。Execute `main.py`.

### `file_watchdog_reg.py`について

`file_watchdog_reg.py`を実行すると、`file_watchdog_reg.py`が置かれているフォルダ内のファイル変更を監視します。ファイルが生成されると、自動で`main.py`が実行されます。

Running `file_watchdog_reg.py` will watch for file changes in the folder where `file_watchdog_reg.py` is located. When a file is created, `main.py` is automatically executed.
