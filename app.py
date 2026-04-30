<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>مفاجأة لحموكشة</title>
    <style>
        body { font-family: 'Arial', sans-serif; text-align: center; background-color: #ffe6e6; padding-top: 100px; }
        h1 { color: #ff4d4d; }
        button { padding: 15px 30px; font-size: 20px; background-color: #ff4d4d; color: white; border: none; border-radius: 25px; cursor: pointer; }
        #message { margin-top: 50px; font-size: 40px; color: #b30000; display: none; }
    </style>
</head>
<body>

    <h1>مفاجأة يا حموكشة! 🎁</h1>
    <p>دوس على الزرار اللي تحت ده عشان تشوف المفاجأة</p>
    
    <button onclick="showMessage()">اضغط هنا</button>

    <div id="message">وحشتني جداً ❤️</div>

    <script>
        function showMessage() {
            document.getElementById('message').style.display = 'block';
        }
    </script>
</body>
</html>
