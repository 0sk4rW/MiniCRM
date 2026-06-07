# MiniCRM Detailing MVP

Celem jest stworzenie systemu CRM dla salonu detailingowego. 
Ma on rozwiązywać problem zarządzania klientami, samochodami i usługami.

Uzytkownikiem tego systemu (na etapie MVP) jest pracownik/właściciel salonu. 
Po konsultacji z klientem wprowadza on do systemu niezbędne dane.


# Planowane funkcje na etapie MVP:

-Dodawać klientów do bazy danych
-Wyświetlać listę klientów
-Dodawanie pojazdów klientów do bazy danych (marka, model, generacja/wersja, rok produkcji)
-Tworzenie zlecenia
-Zmiana statusu zlecenia
-Wyświetlanie listy zleceń
-Przypisywanie usług do zleceń

# Planowane funkcje w późniejszym etapie tworzenia projektu:

-Konta klientow 
-Logowanie uzytkownikow (pracownikow salonu oraz klientow)
-faktury
-kalendarz i rezerwacje terminów
-historia usług
-role i uprwanienia wybranych uzytkownikow
-wyceny i kosztorysy (w późniejszym etapie z pomocą AI ze zdjęć)
-wysyłka sms
-wysyłka e-mail
-generator faktur
-integracje zewnętrzne


# Dane przechowywane w systemie na etapie MVP:

Klient:
-imię
-nazwisko
-numer telefonu
-adres e-mail (opcjonalny)
-notatka

Samochód:
-marka
-model
-generacja / wersja
-rok produkcji 
-numer rejestracyjny
-kolor
-VIN
-notatka

Zlecenie:
-numer zlecenia
-status (Nowe, W trakcie, Gotowe do odbioru, Zakończone, Anulowane)
-data przyjęcia
-planowana data odbioru
-notatka

Usługa:
-nazwa
-cena

# Dane planowane do wykorzystania na późniejszym etapie projektu:

-zdjęć auta
-historii statusów
-płatności
-faktur
-numerów faktur
-kosztów materiałów
-harmonogramu pracowników

# Relacje biznesowe

-Jeden klient może posiadać wiele samochodów.
-Jeden samochód może posiadać wiele zleceń.
-Jedno zlecenie może zawierać wiele usług.
-Jedna usługa może występować w wielu zleceniach.

