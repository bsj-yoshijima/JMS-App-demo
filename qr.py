import cv2
from pyzbar.pyzbar import decode

# QRコード画像を読み込む
def read_qr_code(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)
    
    # QRコードをデコード
    decoded_objects = decode(image)
    
    # 結果を格納する
    results = []
    for obj in decoded_objects:
        results.append(obj.data.decode('utf-8'))  # QRコードの文字列を取得
    
    return results

# テスト実行
if __name__ == "__main__":
    image_path = "example_qr.png"  # QRコード画像ファイルのパス
    qr_results = read_qr_code(image_path)
    
    if qr_results:
        print("QRコードの内容:")
        for result in qr_results:
            print(result)
    else:
        print("QRコードが見つかりませんでした。")


