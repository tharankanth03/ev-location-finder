from fastapi import FastAPI
app = FASTAPI(title='EV Locator & smart Routing API' , version='1.0.0')
@app.get('/health')
def health(): return {'status':'ok'}
