# agent-project-setup: Entscheidungsregister

**Dokumentversion:** 2.0 · **Stand:** 29. Oktober 2026  
**Geltung:** Vollständiger konsolidierter Nachweis Q001–Q121 und ergänzender Aussagen. Keine neuen Nutzerentscheidungen.

## 1. Wie das Register zu lesen ist

Die eingereichten Antworten sind die Grundlage. Frühere Fragen wurden teilweise über eine Oberfläche dargestellt, deren vollständiger Wortlaut im sichtbaren Verlauf nicht enthalten ist. Dieses Register erfindet daher keine Originalfragen und keine unbekannten Optionen. Es dokumentiert die gültige Bedeutung aus Antworten, Präzisierungen und späteren ausdrücklichen Entscheidungen.

«D» bedeutet eine eigene Antwort; der inhaltliche Freitext ist wichtiger als der Optionsbuchstabe. R-Verweise führen zu den Anforderungen in der [Spezifikation](spezifikation.md). Die zugehörigen Prüfungen stehen in [Akzeptanz und Umsetzung](akzeptanz-und-umsetzung.md).

Insbesondere sind Q100/Q101/Q108/Q115 durch **Q120: in memento** aufgelöst; Q106 wird durch **Q110: persönliches GTD in memento** konkretisiert. Das ist keine erneute offene Architekturfrage.

## 2. Die 121 Entscheidungen

### Runde 1: Grundarchitektur

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q001 · C | Ein Repository kann ein einzelnes Projekt oder mehrere Themen und Teilprojekte aufnehmen. **Einordnung:** Die ursprüngliche Antwort lautete nur «Beides wird unterstützt». Diese Bedeutung ist durch den weiteren Verlauf mit memento und eigenständigen Repositories konkretisiert; kein rekonstruierter Fragewortlaut. | R03, R04 |
| Q002 · A | Minimal beginnen: AGENTS.md, Konfiguration und benötigte Skills. Weitere Dokumente nur bei Bedarf. | R03 |
| Q003 · A | Adoption mit adopt-project-setup und versionsbasiertem Sync, analog zum Grundprinzip des Coding-Setups. | R09, R10 |
| Q004 · A | Das Repository ist massgebend. Erkenntnisse aus Gesprächen werden bewusst übernommen. **Einordnung:** Später präzisiert: Ein ausdrücklicher Auftrag oder eine passende dauerhafte bzw. sitzungsbezogene Erlaubnis genügt; keine wiederholte Rückfrage. | R02, R20 |
| Q005 · C | Einheitliche Projektmetadaten, ansonsten freie inhaltliche Struktur. | R03, R05 |
| Q006 · B | Browser-Chats und CLI-Agenten fachlich gleichwertig unterstützen. **Einordnung:** Nicht mit identischen technischen Rechten oder automatischem Repository-Zugriff gleichsetzen. | R29, R35, R40 |

### Runde 2: Struktur und Zusammenarbeit

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q007 · C | Zentrale Übersicht; Teilprojekte nur bei Bedarf mit zusätzlicher Konfiguration. | R04, R05 |
| Q008 · A | Das gewählte Format ist der Standard für neue Dokumente. Bestehende gemischte Bestände bleiben erlaubt. | R06 |
| Q009 · C | Beim Formatwechsel wählen: nur Standard umstellen oder vorhandene Inhalte kontrolliert migrieren. | R07 |
| Q010 · B | Nur Projekte haben verbindliche Metadaten; Dokumentmetadaten entstehen bei Bedarf. | R05 |
| Q011 · B | Nur einen minimalen Einstieg laden und weitere Informationen gezielt nachlesen. | R18 |
| Q012 · C | Bei aktiver Arbeit Änderungen vorschlagen oder vorbereiten; verbindliche neue Entscheidungen bewusst bestätigen. **Einordnung:** Bereits bestätigte Entscheidungen und eindeutig freigegebene Captures nicht nochmals bestätigen lassen. | R20, R30 |
| Q013 · B | Gemeinsame Dateien und fachliche Workflows; unterschiedliche technische Wege für Browser und CLI. | R35, R40 |
| Q014 · C | Ein gemeinsamer Einstiegspunkt und getrennte Verantwortungsbereiche. Syncs überschreiben keine fremden Inhalte. | R01, R08 |

### Runde 3: Wissen, Skills und Lebenszyklus

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q015 · B | Bestehende Artikel gezielt ergänzen statt unnötige Duplikate anzulegen. | R12 |
| Q016 · B | Passende Links bei Änderungen ergänzen; keine neuen Artikel nur zum Erzeugen von Links. | R12 |
| Q017 · B | Externe Fakten und Forschung nachvollziehbar belegen. Persönliche Beobachtungen benötigen keine künstlichen Quellen. | R12 |
| Q018 · B | Widersprüche kennzeichnen, Belege vergleichen und Aktualisierung vorschlagen. | R12 |
| Q019 · B | Minimaler Skill-Kern; zusätzliche Skills bei Bedarf auswählen. | R11, R38 |
| Q020 · B | Skills versioniert übernehmen, Herkunft dokumentieren und Updates kontrolliert anbieten. | R10, R11 |
| Q021 · C | Vorhaben im Wiki beginnen oder bewusst in ein eigenes Repository auslagern. | R04, R28 |
| Q022 · B | Org, Markdown oder Issue-Tracker sind mögliche Aufgabenquellen; je Aufgabenbestand gibt es eine massgebende Quelle. **Einordnung:** Q110 legt für das persönliche GTD memento fest. Externe technische Tickets bleiben verlinkte, eigenständige Bestände. | R14 |
| Q023 · B | Ein Journal für Aktivitäten, Beobachtungen und Fortschritt ist optional. **Einordnung:** Später in persönliches Journal und KI-Aktivitätsjournal getrennt. | R23 |

### Runde 4: Adoption und Updates

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q024 · B | Bestand analysieren, Integrationsplan und Konflikte zeigen, anschliessend kontrolliert übernehmen. | R09 |
| Q025 · A | Projektkonfiguration zentral in einer maschinenlesbaren Datei, beispielsweise .agent-project.conf. **Einordnung:** Konkreter Dateiname und Serialisierungsformat bleiben technische Ausgestaltung. | R05 |
| Q026 · B | Jedes Setup besitzt eigene Regeldateien; AGENTS.md ist der gemeinsame Einstiegspunkt. | R08 |
| Q027 · B | Updates anbieten, Unterschiede zeigen und erst nach Zustimmung anwenden. | R10 |
| Q028 · B | Konflikte melden und gezielt zusammenführen; nie stillschweigend überschreiben. | R10, R22 |
| Q029 · D: B + Ergänzung | Auch nur in einem Projekt benötigte lokale Skills zulassen; sie müssen nicht ins zentrale Setup. | R11 |
| Q030 · D: A, C bewusst möglich | Coding-Setup im bestehenden Projekt ergänzen oder bei bewusster Entscheidung ein eigenes Software-Repository verwenden. **Einordnung:** Konsolidiert anhand der Nutzerpräzisierung und des späteren Handoff-Vertrags, nicht anhand unbekannter Originaloptionen. | R01, R28 |
| Q031 · B | Git und Dateien bilden die Grundlage; GitHub-spezifische Funktionen sind optionale Adapter. | R35 |
| Q032 · B | Standardisierte Kontext- und Änderungspakete für den Wechsel zwischen Umgebungen bereitstellen. | R40 |

### Runde 5: Wiki und Natural Planning

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q033 · B | Methoden optional und flexibel anbieten; die KI empfiehlt passende Schritte. | R13 |
| Q034 · B | Leichter Wissensworkflow: Fragestellung, vorhandenes Wissen, Quellen, Erkenntnisse und offene Fragen. | R12 |
| Q035 · C | KI darf ein Vorhaben als Projekt vorschlagen; der Nutzer bestätigt die Umwandlung ausdrücklich. | R13 |
| Q036 · D: B + laufend optimieren | Natural Planning als schlanken Leitfaden verwenden und anhand der Praxis verbessern. | R13, R31 |
| Q037 · C | Tiefe adaptiv wählen: nur die für das konkrete Vorhaben nötigen Fragen stellen. | R13 |
| Q038 · B | Zweck und Ergebnisbild im Projektkontext, konkrete Aufgaben in der gewählten Aufgabenquelle halten. | R13, R14 |
| Q039 · B | Relevante vorhandene Inhalte prüfen und Artikel, Links sowie Quellen gezielt pflegen. | R12, R18 |
| Q040 · B | Wiederverwendbare Methoden ins zentrale Setup; projektspezifische Methoden bleiben lokal. | R11, R31 |

### Runde 6: KI-Zusammenarbeit und Git

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q041 · B | Verbesserungsideen während der Arbeit im Projekt-Backlog sammeln und später gezielt ans Setup geben. | R31 |
| Q042 · B | KI schlägt zuständiges Setup oder Skill vor; der Nutzer bestätigt die Zuordnung. | R31 |
| Q043 · B | Prägnant und vollständig schreiben: keine Wiederholungen oder Fülltexte, alle entscheidungsrelevanten Informationen erhalten. | R39 |
| Q044 · B | Änderungen am Ende eines Arbeitsschritts gesammelt melden: Dateien, Inhalt und offene Prüfungen. | R30, R39 |
| Q045 · B | Logisch zusammengehörige Änderungen sammeln und nach einem sinnvollen Arbeitsschritt committen. | R30 |
| Q046 · B | Kleine risikoarme Änderungen dürfen direkt auf main; grössere oder riskante über Branch und Review/PR. **Einordnung:** Strengere Projekt- oder Branchschutzregeln bleiben wirksam. | R30 |
| Q047 · B | Issues für geplante oder grössere Arbeit; kleine Änderungen ohne Issue erledigen und über Git dokumentieren. | R14, R30 |
| Q048 · D: B + Handoff anbieten | Sitzungsabschluss mit offenem Stand und nächsten Schritten; ein Handoff anbieten, nicht ungefragt erstellen. | R29, R30 |

### Runde 7: Schutz, Sicherung und Migration

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q049 · A | Jedes Projekt hat die Schutzstufe öffentlich, privat oder vertraulich. | R32 |
| Q050 · B | Datenklassifikation beachten; eine neue externe Übermittlung vertraulicher Inhalte ausdrücklich freigeben lassen. | R20, R32 |
| Q051 · D: B + Hosting-Frage | Backups nach Bedeutung und Hosting vorsehen; unabhängige Sicherung und späteres Forgejo-Selbsthosting berücksichtigen. **Einordnung:** Clones und Sync sind nützlich, aber keine vollständige Sicherungsstrategie. Kein Selbsthosting-Projekt in V1. | R34 |
| Q052 · C | Konvertierung nur mit Vorschau, Prüfbericht und expliziter Freigabe; nicht übertragbare Inhalte erhalten oder separat behandeln. | R07 |
| Q053 · B | Formatmigration für gesamtes Repository, Verzeichnis oder ausgewählte Dateien unterstützen. | R07 |
| Q054 · B | Links und Referenzen erhalten und validieren; Besonderheiten im Migrationsbericht ausweisen. | R07, R35 |
| Q055 · B | Kleine Änderungen im vereinbarten Rahmen erlauben; Löschungen, Massenänderungen und riskante Migrationen vorher freigeben lassen. | R20, R22, R32 |
| Q056 · D: B + Selbsthosting/Text | Originale nach Bedarf behandeln und geeignete Informationen als Text erschliessen. **Einordnung:** Selbsthosting hebt die Notwendigkeit einer Speicher- und Sicherungsstrategie nicht auf; keine unbeprüfte Gleichsetzung von Extrakt und Original. | R33 |

### Runde 8: Privat/Geschäftlich und Skills

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q057 · A | Privat oder geschäftlich ist ein Pflichtfeld, getrennt von der Vertraulichkeitsstufe. | R05, R32 |
| Q058 · B | Privat und Geschäftlich standardmässig strikt trennen; projektübergreifende Übernahmen brauchen ausdrückliche Freigabe. **Einordnung:** Das reine Auflösen einer freigegebenen Zuständigkeit ist keine Erlaubnis, Quellinhalte zwischen Schutzbereichen zu kopieren. | R27, R32 |
| Q059 · D: B + Geräte-Sync | Laptop und Android/Termux mit Git nutzen; bestehendes gs-Skript als Ausgangspunkt für sicheren geräteübergreifenden Sync prüfen. | R34, R35 |
| Q060 · B | Original und Textfassung verknüpfen; Originale je nach Bedarf in Git, LFS oder extern ablegen. | R33 |
| Q061 · D: B + eigene Skills | Matt-Pocock- und AIHero-Methoden auf Eignung prüfen; eigene Wiki- und Projekt-Skills sind ausdrücklich erlaubt. **Einordnung:** Keine ungeprüfte Übernahme von Coding-Annahmen; Verbesserungen für Coding separat behandeln. | R11 |
| Q062 · C | Gemeinsamer Arbeitsablauf: Informationen aufnehmen, strukturieren, dokumentieren und Kontext pflegen. | R12, R18, R20 |
| Q063 · B | Passende installierte Skills selbst auswählen; umfangreiche oder stark eingreifende Abläufe vorher vorschlagen. | R11, R20 |
| Q064 · B | Vorhandene Methoden analysieren und erhalten, bei Bedarf durch passende Skills ergänzen. | R03, R11 |

### Runde 9: Praxistests und Synchronisation

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q065 · D: Menüplaner und Chat-Umzug | Menüplaner mit vorhandenem Brainstorming als erster Pilot; persönliche Chat-Projekte aus dem Business-Account als weiterer Übernahmefall. **Einordnung:** Private Inhalte selektieren; kein automatischer Transfer eines gesamten Business-Exports. | R38 |
| Q066 · C | Kombination mit dem Coding-Setup erst praktisch testen, wenn ein reales Projekt sie braucht. **Einordnung:** Die Kombinationsfunktion darf erst nach bestandenem Integrationstest als unterstützt gelten; der Kernpilot wird nicht blockiert. | R01, R37, R38 |
| Q067 · D: ausserhalb KI, Laptop und Handy | Git-Sync als eigenständiges, KI-unabhängiges Vorhaben und Repository; gs verbessern oder ersetzen. | R34 |
| Q068 · B | Vor Sync lokale Änderungen prüfen; sichere Schritte automatisieren, Konflikte zur Entscheidung melden. | R22, R34 |
| Q069 · C | Merge/Rebase darf automatisch versucht werden; bei ungelösten Konflikten stoppen. **Einordnung:** Keine Veränderung geteilter Historie oder Force-Push ohne eigene ausdrückliche Freigabe. | R34 |
| Q070 · B | Format, interne Links, Metadaten und relevante Regeln automatisiert prüfen; Inhalte fachlich kontrollieren, wo nötig. | R37 |
| Q071 · B | Git- und Dateifunktionen sofort hostunabhängig halten; Forgejo-Integration später testen. | R35, R38 |
| Q072 · B | Neue und bestehende Projekte, Org/Markdown, Skills, Sitzungswechsel, Updates und parallele Setups nachweislich prüfen. **Einordnung:** Nachweise je Ausbaustufe, nicht pauschal für noch nicht implementierte optionale Funktionen behaupten. | R37, R38 |

### Runde 10: Projekt-Auslagerung

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q073 · C | Bei Auslagerung relevante Inhalte analysieren, gezielt übernehmen, strukturieren und Herkunft dokumentieren. | R28 |
| Q074 · D + spätere Präzisierung | Nach bestätigter Auslagerung im neuen Repository weiterarbeiten. Wiki erhalten und dort mit Zeitstempel, Link und Zuständigkeit auf den neuen Ort verweisen. | R02, R28 |
| Q075 · B | Handoff umfasst Ziele, Wissen, Entscheidungen, Quellen, verworfene Alternativen, Feature-Ideen, offene Fragen und nächste Schritte. | R28 |
| Q076 · D: B + spontaner Chat | Ein zunächst flüchtiges Gespräch kann auf Wunsch in dauerhaftes Projektwissen überführt werden. | R20, R29 |
| Q077 · B | Wiederverwendbares Wissen erkennen und Übernahme ins passende Wiki oder Setup vorschlagen. | R27, R31 |
| Q078 · B | Standardmässig Repository-Kontext verwenden; nur bei Bedarf kompaktes portables Handoff anbieten. | R29, R40 |
| Q079 · B | Übergabe erst nach Prüfung von Inhalten, Links, Quellen und Projektstatus sowie Nutzerbestätigung abschliessen. | R28, R37 |

### Runde 11: Technische Grundarchitektur

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q080 · B | AGENTS.md gehört ausschliesslich dem Projekt; Setups verwalten eigene Regeln und kontrolliert ihre Verweise. | R08 |
| Q081 · B | Verbindliche Metadaten umfassen zusätzlich Projekttyp, Aufgabenquelle und Setup-Version. | R05 |
| Q082 · B | Unterprojekte erben Standards, dürfen Format, Aufgabenquelle und eigene Anweisungen gezielt überschreiben. **Einordnung:** Dies erlaubt keine stillschweigende Lockerung technischer Zugriffs- oder Datenschutzgrenzen. | R04, R05 |
| Q083 · D: aktuell B | Dateibasierte Aufgaben langfristig ermöglichen; kein eigener vollwertiger Tracker in der ersten Version. **Einordnung:** Q91 konkretisiert V1 auf vorhandene TODOs und Checklisten; Kommentare, Reviews und GUI bleiben ein optionales Folgeprojekt. | R14, R38 |
| Q084 · B | Zentrale Skills versioniert übernehmen; lokale Skills separat verwalten; agentenspezifische Pfade sind Adapter. | R11 |
| Q085 · B | Gespräch analysieren, Projekt vorschlagen und nach Freigabe Dateien oder Repository vorbereiten. | R20, R29 |
| Q086 · B | Kleiner durchgängiger Kern: Adoption, Kontextpflege, Formatwahl, Update, Handoff; weitere Skills schrittweise. | R38 |

### Runde 12: Schnittstellen und erster Abschluss

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q087 · A | Nötige Anpassungen am Coding-Setup sind zulässig, aber rückwärtskompatibel und unabhängig vom neuen Setup. | R01, R08 |
| Q088 · B | AGENTS.md enthält Projektregeln und Verweise; Setup-Skills bearbeiten nur ihre Verweise kontrolliert mit Konfliktprüfung. | R08 |
| Q089 · A | Setup-Verbesserungen ohne Projektdaten zusammenfassen und vor Übernahme prüfen. | R31, R32 |
| Q090 · A | Erste Umsetzung auf Adoption, Updates, Kontextpflege und Projekt-Handoff konzentrieren. | R38 |
| Q091 · A | Eine eigene dateibasierte Aufgaben- und Review-Lösung ausdrücklich vormerken, V1 aber auf bestehende TODOs und Checklisten begrenzen. | R14, R38 |
| Q092 · A | Entscheidungen konsolidieren, Widersprüche und offene technische Punkte dokumentieren, Spezifikation vorlegen. **Einordnung:** Die Grundarchitektur wurde danach ausdrücklich bestätigt; weitere Runden erweiterten sie. | R37 |

### Runde 13: Capture, GTD und Journale

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q093 · D: B + müheloses Ablegen | KI-Capture soll freigegebene Informationen möglichst unmittelbar richtig ablegen; das Journal macht die tatsächlichen Änderungen prüfbar. | R20, R23 |
| Q094 · D: B + SQLite/Alternativen | orgfdb bevorzugt auf Nutzen prüfen; schneller SQLite-Rebuild ist akzeptabel, rg/ug können gezielte Textsuche ergänzen. | R17, R18 |
| Q095 · D: B + nichts vergessen | Möglichst wenige relevante Aufgaben zeigen; gelegentlich systematisch nach übersehenen Verpflichtungen suchen. | R15, R16 |
| Q096 · B | INBOX-Review nach Bedarf aktiv vorschlagen; SOMEDAY in grösseren Abständen prüfen. | R16 |
| Q097 · B | Alte Aktivitätseinträge archivieren; normale Ansicht auf aktuelle Einträge begrenzen. **Einordnung:** Q102 legt 30 Tage fest, nicht Löschung persönlicher Journale. | R24 |
| Q098 · B | Aktivitätseintrag enthält Kurzbeschreibung, Zeitstempel, Ziel und Link; Commit-Referenz ist optional. | R23, R25 |
| Q099 · D: B + Links, knapp | Persönliches Journal kurz und prägnant halten; auf anderweitig abgelegte Inhalte verlinken. | R23, R39 |
| Q100 · D: B oder A; später entschieden | KI-Aktivitäten zentral auf einen Blick prüfen können. **Einordnung:** Der damals offene Ort ist durch Q120 abschliessend memento. | R19, R23 |

### Runde 14: Zentrale Übersicht und Speicher

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q101 · D: B + beim Index | Projektindex und zentrale Aktivitätsübersicht sollen zusammengehören. **Einordnung:** Nicht mehr auf die zwischenzeitlich vorgeschlagene separate XDG-Verwaltungsstruktur festlegen; Q120 ist massgebend. | R19, R23 |
| Q102 · B | 30 Tage in der aktuellen Aktivitätsansicht; ältere Einträge archivieren. | R24 |
| Q103 · D: B + Diff | Änderungen sollen über Diffs nachvollziehbar sein. **Einordnung:** Q109/Q116 vereinfachen dies auf Git-Diffs ohne zusätzliche dauerhafte Snapshot-Datenbank. | R25 |
| Q104 · D: A + Watch | Schnellen Rebuild und vorhandenen Watch-Modus von orgfdb verwenden; Aktualität nach Änderungen beachten. | R17 |
| Q105 · D: B + Org/WebP | Geeignete PDF- und DOCX-Inhalte nach Org umwandeln, Bilder gegebenenfalls als WebP optimieren und weitere Löschkandidaten bei Migration prüfen. **Einordnung:** Kein Office-Programm voraussetzen; Originale erst nach geprüfter Freigabe löschen. | R33 |
| Q106 · D: B, eventuell A | Persönliche Aufgaben je externem Projekt in memento führen und genau verlinken. **Einordnung:** Q110 entscheidet abschliessend: persönliches GTD ausschliesslich in memento; keine doppelte technische Aufgabenpflege. | R14 |
| Q107 · D: B + erinnern | Auf ausstehende relevante Prüfungen/Migrationsarbeit hinweisen. **Einordnung:** Der vollständige ursprüngliche Fragetext ist nicht sichtbar. Keine konkrete Taktung oder Hintergrundautomatisierung daraus ableiten; Hinweise bei zugänglichen offenen Einträgen und Reviews. | R16, R33 |

### Runde 15: Vereinfachung und Werkzeugwahl

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q108 · D: doch in memento? | Persönliche Verwaltungsinformationen sollen möglichst in memento bleiben. **Einordnung:** Zwischenzeitliche Rückfrage, endgültig durch Q120 entschieden. | R19, R23 |
| Q109 · D: einfach, Diff-Ziel? | Diff-Nachweis einfach halten und nicht auf Emacs festlegen. **Einordnung:** Q116 entscheidet Git-Diffs; terminal-, editor- oder hostseitige Anzeige ist austauschbar. | R25, R35 |
| Q110 · A | Persönliche GTD-Aufgaben ausschliesslich in memento; externe Projektaufgaben über Links referenzieren. | R14 |
| Q111 · D: A + Erklärung erbeten | Fehlenden Schreibzugriff mit offenem Capture statt vorgetäuschtem Speichern behandeln. **Einordnung:** Kein vollständiger Projekt-Handoff; Q117 legt das konkrete Fallback fest. | R21, R29 |
| Q112 · D: B + Beispiele | Org-Dateien und CLI als Grundlage, Emacs nicht zwingend. **Einordnung:** Beispiele wurden zur Verdeutlichung erbeten; keine eigene mobile App oder neue GUI beauftragt. | R35 |
| Q113 · B | Inventarisieren, Duplikate/Löschkandidaten vorschlagen, geeignete Inhalte nach Org konvertieren und Bilder optimieren; Originale erst nach Freigabe löschen. | R33 |
| Q114 · B | Projektübergreifende Hilfe optional und lokal nutzbar halten; jedes Repository bleibt ohne sie funktionsfähig. | R19, R35, R38 |

### Runde 16: Persistenz und letzte Vereinfachung

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q115 · D: Ort erneut offen | Ort von Index und Journal nochmals klären. **Einordnung:** Keine bleibende offene Architekturfrage: Q120 entscheidet memento. | R19, R23 |
| Q116 · B | Git-Diffs nutzen; nur bei wichtigen uncommitteten Änderungen eine Vorschau anbieten. | R25 |
| Q117 · B | Falls möglich Capture in memento-INBOX speichern; sonst exportierbaren Eintrag anbieten und als noch offen kennzeichnen. | R21 |
| Q118 · D: A + CUSTOM_ID | Neue Org-Überschriftenlinks bevorzugt mit CUSTOM_ID und Dateikontext erstellen statt von globalem ID-Index abhängig zu sein. **Einordnung:** Die Nutzeraussage zur funktionierenden GitHub-Darstellung wird respektiert; konkrete Renderer trotzdem in der Integration prüfen, keine Garantie für jede App. | R35 |
| Q119 · A | Vorerst vorhandene Org-Dateien, orgfdb, Git und wenige Skills verwenden; keine neue umfassende Anwendung bauen. | R38 |

### Runde 17: Abschlussentscheidungen

| Frage / Antwort | Gültige Entscheidung und Präzisierung | Anforderungen |
| --- | --- | --- |
| Q120 · A | Projektindex, Aktivitätsjournal und Capture-INBOX in memento führen. Andere Repositories bleiben eigenständig. | R19, R21, R23 |
| Q121 · B | Bei passenden Gesprächen auf offene Captures hinweisen, sofern die KI auf deren Liste zugreifen kann. **Einordnung:** Kein Verlass auf plattforminternes Gedächtnis und kein versprochener Hintergrundlauf ohne tatsächliche Automatisierung. | R16, R21 |

## 3. Ergänzende Entscheidungen ausserhalb der nummerierten Antworten

### E01: Zwei eigenständige Setups, kein drittes Wiki-Setup

Wiki- und Projektmethoden bleiben optionale Arbeitsweisen von agent-project-setup. coding-agent-setup bleibt unabhängig. Eine separate Wiki-App wird nicht vorausgesetzt.

**Zuordnung:** R01, R04, R11, R38.

### E02: Memento ist Wiki und Projektumgebung

Die Themenliste ist ein Index zu Notes; Notes, Natural-Planning-Projekte und Aufgaben sind bereits vorhanden. Rund 400 MB sind eine Nutzerangabe, keine gemessene Tokenmenge. Keine vorsorgliche Aufteilung oder neue Ordnerhierarchie.

**Zuordnung:** R03, R04, R18.

### E03: Gesundheit und Lernplattform können eigenständig sein

Ein in sich grosses Patientendossier oder ein ausgearbeitetes Projekt darf ausgelagert werden. Der Handoff bewahrt die investierte Vorarbeit; keine starre Grenze nach allgemeinen vs. persönlichen Gesundheitsthemen erzwingen.

**Zuordnung:** R02, R28, R32.

### E04: Situative Capture-Vorschläge und vorab erteilte Erlaubnis

Standardmässig situativ anbieten. Für bestimmte Themen oder eine laufende Sitzung darf der Nutzer direktes Speichern erlauben. Ein eindeutiger Ziel- und Speicherauftrag braucht keine zweite Freigabe. Gefährliche Operationen sind nicht mitgemeint.

**Zuordnung:** R19, R20, R21.

### E05: Luna High war ein Umsetzungsprofil

Der Nutzer hatte vor Sol Medium Luna High für die Umsetzung verwendet und möchte wieder wechseln können. Der Wunsch nach xHigh bleibt eine wählbare, explizit freizugebende Variante. Keine pauschale Aussage zu aktuellen Modellpreisen, API-IDs oder Verfügbarkeit.

**Zuordnung:** R26.

### E06: Sieben Org-TODO-Keywords

INBOX, SOMEDAY, TODO, NEXT, WAIT, DONE und CANCEL bleiben erhalten. NEXT/WAIT sollen knapp sichtbar sein, gesnoozte Inhalte nicht ständig auftauchen. Regelmässige Vollständigkeitsprüfung verhindert, dass Aufgaben verschwinden.

**Zuordnung:** R14, R15, R16.

### E07: Kalendergedanke bleibt optional

Eine spätere Google-Calendar-Anbindung ist interessant; kein bestehender Kalender wird abgeschafft. Es wurde kein Termin, Scheduler oder wiederkehrender Review beauftragt.

**Zuordnung:** R16, R36, R38.

### E08: Bestehendes orgfdb wiederverwenden

Rust-CLI mit SQLite, schnellem Rebuild und Watch-Mode soll für Headings, Links, Dateien und Aufgaben geprüft werden. Strukturabfragen und gezielte Textsuche können sich ergänzen; kein neuer Suchserver als Standard.

**Zuordnung:** R17, R18, R38.

### E09: Zwei Journale und zentraler Überblick

KI-Änderungen und persönliche Erlebnisse sind getrennte Inhalte. Zentrale KI-Aktivitätsansicht in memento, 30 Tage aktuell, danach Archiv; kurze Links statt Inhaltskopien.

**Zuordnung:** R23, R24, R25.

### E10: CUSTOM_ID statt neuer globaler ID-Pflicht

Neue Heading-Links bevorzugen CUSTOM_ID mit Dateikontext. Bestehende IDs nicht pauschal umschreiben. Die vom Nutzer beobachtete GitHub-HTML-Unterstützung ersetzt nicht den Test anderer Viewer.

**Zuordnung:** R35.

### E11: Linux, Laptop und Android

Linux/Bash als Setup-Ziel; keine neuen Windows- und WSL- und PowerShell-Anleitungen. Termux für Git bleibt relevant. Emacs und eine konkrete Handy-App sind austauschbar; keine eigene App im ersten Umfang.

**Zuordnung:** R34, R35, R38.

### E12: Einfacher Git-Workflow, optionale Tracker-Idee

Kleine Änderungen nicht in zahllose Issues/PRs zerlegen. Ein lokaler Tracker mit Kommentaren, Diffs, Reviews und zeitlicher Priorisierung/SOMEDAY ist eine interessante separate Idee, keine Implementierungsabhängigkeit.

**Zuordnung:** R14, R25, R30, R38.

### E13: Medienmigration ohne Office-Pflicht

Geeignete PDF- und DOCX-Inhalte nach Org, geeignete Bilder optimieren. Duplikate und Löschkandidaten vorschlagen; Originale nicht ungeprüft entfernen. GitHub-Grössenempfehlungen nicht mit einem harten 1-GB-Maximum verwechseln.

**Zuordnung:** R33.

### E14: Gespeichert ist nicht gemerkt

Ein nur im Chat stehender Capture ist kein verlässliches späteres Arbeitsgedächtnis. Nur persistente erreichbare Listen können später geprüft werden. Ohne Zugriff weder Erinnerung noch Speicherung behaupten.

**Zuordnung:** R16, R21, R40.

### E15: Prägnanz und bessere Methoden

Texte kurz und entscheidungsrelevant halten, ohne wesentliche Informationen zu verlieren. Wiederverwendbare Verbesserungen sammeln und sanitisiert ans zuständige Setup bzw. Skill zurückmelden.

**Zuordnung:** R31, R39.

### E16: Dokumentationsauftrag nach Pro-Wechsel

Nach Abschluss Q121 ist jetzt die konsolidierte Spezifikation beauftragt. Kein Auftrag für Repository-Anlage, Issues, Produktcode oder automatische Konfiguration.

**Zuordnung:** R37, R38.

## 4. Was nicht stillschweigend weitergilt

Frühere Vorschläge für ein separates globales Konfigurations- und Journalverzeichnis sind durch Q120 ersetzt. Eine pauschale Bestätigung vor jedem Capture ist durch die späteren begrenzten Schreibfreigaben ersetzt. Eine zentrale Kopie aller technischen Projektaufgaben ist nicht beschlossen. Ein starres Sol- oder Luna-Modell ist nicht beschlossen. Eine eigene permanente Diff- und Snapshot-Engine ist nicht beschlossen. Ein automatisch laufender Reminder oder Kalender-Sync ist nicht eingerichtet und nicht beauftragt.

Technische Verträge wie das genaue Konfigurationsschema, die orgfdb-Frischeprüfung oder die Journaldatei-Namen stehen in TP01–TP14 der Spezifikation. Sie sind Ausgestaltungsarbeit, keine Erlaubnis, die geklärten Nutzerentscheidungen neu zu erfinden.
