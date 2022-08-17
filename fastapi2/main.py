from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        'titulo': 'Django',
        'aulas': 10,
        'horas': 10
    },
    2: {
        'titulo': 'FastAPI',
        'aulas': 5,
        'horas': 5
    },
}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({'id': curso_id})

    return curso

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0',
                port=8000, debug=True, reaload=True)
