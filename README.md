# Locust Performance Testing Framework

Projekt przedstawia praktyczne zastosowanie narzędzia **Locust** do przeprowadzania testów wydajnościowych i obciążeniowych (Load Testing) dla REST API.

##  Technologie
- **Język:** Python 3.x
- **Narzędzie:** Locust

##  Funkcjonalności
- Symulacja setek równoczesnych użytkowników (Concurrent Users).
- Analiza parametrów **RPS** (Requests Per Second) oraz **Response Time**.
- Monitorowanie błędów serwera pod obciążeniem w czasie rzeczywistym.
- Testowanie różnych punktów końcowych (endpoints) z różną wagą priorytetu (`@task`).

##  Jak uruchomić
1. Zainstaluj wymagania: `pip install -r requirements.txt`
2. Uruchom Locust: `locust`
3. Otwórz panel webowy: `http://localhost:8089`