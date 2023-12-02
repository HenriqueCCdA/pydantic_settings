# pydantic_settings

Simulando alguns o comportamentos do `python-decouple` com o `pydantic-settings`.

O objeto `settings` possui duas configuarações. O inteiro `SCALAR` e `LISTA`. O `SCALAR`é obrigatorio, já `LISTA` tem um valor padrão

```python
class Settings(BaseSettings):
    SCALAR: int
    LISTA: tuple[str, ...] = ('default',)
```

A lista pode espera valores separados por virgulas. Por Exemplo, `"banana,maça,pera"`. 

Além disso a variaveis de ambiente tem precedencia sobre o arquivo `.env`.

