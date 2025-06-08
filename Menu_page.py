# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

allergy_dict = {
    1: "난류", 2: "우유", 3: "메밀", 4: "땅콩", 5: "대두", 6: "밀",
    7: "고등어", 8: "게", 9: "새우", 10: "돼지고기", 11: "복숭아", 12: "토마토",
    13: "아황산류", 14: "호두", 15: "닭고기", 16: "쇠고기", 17: "오징어",
    18: "조개류", 19: "잣"
}

menu_data = {
    "5/26": [
        {"menu": "미트소스스파게티", "allergies": [1,2,5,6,10,12,13,15,16]},
        {"menu": "추가밥", "allergies": []},
        {"menu": "함박스테이크", "allergies": [1,2,6,10,12,13,15,16]},
        {"menu": "매쉬드포테이토", "allergies": [5,6]},
        {"menu": "오이피클", "allergies": [13]},
        {"menu": "깍두기", "allergies": [9,13]},
    ],
    "5/27": [
        {"menu": "현미밥", "allergies": []},
        {"menu": "부대찌개", "allergies": [5,6,10,13]},
        {"menu": "순살안동찜닭", "allergies": [5,6,15]},
        {"menu": "부추전*초간장", "allergies": [5,6]},
        {"menu": "백김치", "allergies": [9,13]},
        {"menu": "방울토마토", "allergies": [12]},
    ],
    "5/28": [
        {"menu": "백미밥", "allergies": []},
        {"menu": "나가사끼짬뽕", "allergies": [5,6,10,13,17,18]},
        {"menu": "후후츠탕수육", "allergies": [5,6,10,12,13]},
        {"menu": "두부조림", "allergies": [5,6]},
        {"menu": "꼬들단무지", "allergies": [13]},
        {"menu": "포기김치", "allergies": [9,13]},
    ],
    "5/29": [
        {"menu": "기장밥", "allergies": []},
        {"menu": "어묵국", "allergies": [5,6]},
        {"menu": "돈사태장조림", "allergies": [5,6,10]},
        {"menu": "고구마튀김*간장", "allergies": [5,6]},
        {"menu": "깍두기", "allergies": [9,13]},
        {"menu": "오렌지", "allergies": []},
    ],
    "5/30": [
        {"menu": "나물비빔밥*양념장", "allergies": [5,6]},
        {"menu": "순두부찌개", "allergies": [5,6,10]},
        {"menu": "순살치킨", "allergies": [1,2,5,6,13,15]},
        {"menu": "콘샐러드", "allergies": [1,5,6,13,15]},
        {"menu": "포기김치", "allergies": [9,13]},
        {"menu": "한국요구르트", "allergies": [2]},
    ]
}

def check_allergy(user_allergies):
    warnings = {}
    for day, menus in menu_data.items():
        matched = []
        for item in menus:
            if any(a in user_allergies for a in item["allergies"]):
                matched.append(item["menu"])
        if matched:
            warnings[day] = matched
    return warnings

@app.route("/", methods=["GET", "POST"])
def index():
    warning_data = {}
    selected = []
    if request.method == "POST":
        selected = request.form.getlist("allergies")
        try:
            selected = [int(x) for x in selected if x.strip().isdigit()]
        except ValueError:
            selected = []
        warning_data = check_allergy(selected)

    return render_template("index.html", allergy_dict=allergy_dict, menu_data=menu_data,
                           warning_data=warning_data, selected=selected)

if __name__ == "__main__":
    app.run(debug=True)
