from flask import Flask, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

students = ['Смелкин Н.Д. БСБО-02-20',
            'Рулев Д.О. БСБО-02-20',
            'Ребров М.Е. БСБО-02-20',
            'Сидоров М.М. БСБО-02-20',
            'Смирнов Д.С. БСБО-02-20',
]

for student in students:
    r.rpush('students', student)

print('Getting students from Redis...')

@app.route('/')
def index():
    students = r.lrange('students', 0, -1)
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2517)
