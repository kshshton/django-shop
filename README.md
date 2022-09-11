# Todo list
- ##### Autoryzacja użytkowników
- ##### Dodawanie produktów na stronę
- ##### Podgląd produktu
- ##### Dodawanie produktu do koszyka
- ##### Funkcjonalność koszyka
- ##### Funkcjonalność płatności
- ##### Rejestracja
- ##### Logowanie
- ##### Dodawanie środków na konto
- ##### Generowanie id zamówienia
- ##### Historia zamówień
- ##### Panel administratora
- ##### Przejrzysty szablon strony
- ##### Opdowiednie relacje SQL
- ##### Rekordy zapisywane w bazie danych

<br />

## Uruchamianie projektu
### Virtual environment (dependencies)
>##### Linux, Mac 
```bash
source venv/bin/activate
```

>##### Windows
```powershell
set-executionpolicy remotesigned
```
```python
python windows_path.py
```
```powershell
.\venv-windows\Scripts\Activate.ps1
```
### Creating admin account
```bash
python manage.py createsuperuser
```
### Local server
```bash
python manage.py runserver
```
