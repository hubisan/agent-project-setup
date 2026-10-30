# agent-project-setup: Akzeptanz und Umsetzungsreihenfolge

**Dokumentversion:** 2.0 · **Stand:** 29. Oktober 2026  
**Zugehörig:** [Spezifikation](spezifikation.md) und [Entscheidungsregister](entscheidungsregister.md).

## 1. Status und Testprinzip

Alle nachfolgenden Produktprüfungen sind **geplant, nicht durch diese Dokumenterstellung ausgeführt**. Das Lesen von README- und CLI-Dokumentation ist kein Laufzeit- oder Integrationstest.

Geprüft wird sichtbares Verhalten an möglichst hohen Schnittstellen: freigegebener Auftrag hinein, nachvollziehbare Datei- und Kontextänderung und Ergebnisbericht heraus. Kleine deterministische Prüfungen für Konfiguration, Links, Capture-Deduplikation und Zustandsfilter ergänzen diese Abläufe. Tests sollten nicht an interne Klassen oder eine noch nicht gewählte Implementierung gekoppelt werden.

Für destruktive, fehlerhafte oder vertrauliche Szenarien werden Wegwerf-Repositories und synthetische Daten verwendet. Echte private Daten werden nur nach gezielter Freigabe als Pilotbestand verwendet. Tests senden keine solchen Daten an neue externe Dienste.

## 2. Abnahmegrenzen

| Stufe | Nachweis | Nicht als Voraussetzung vorziehen |
| --- | --- | --- |
| V1-A Kern | Neue/bestehende Repositories, Rechte/Metadaten, Formate, Kontext, Skills, Updates, Handoff, ehrlicher Bericht; Menüplaner-Pilot | Vollständiges GTD, Kalender, neue GUI, eigener Sync |
| V1-B memento | Erhalt der echten Note- und Indexstruktur; orgfdb; Projektindex; Capture- und INBOX-Persistenz; Journale; GTD/Reviews | Eine eigene mobile App oder ein globaler Suchserver |
| Coding-Kombination | Beide Installationsreihenfolgen, getrennte Updates, lokale Skills und Agenten-Ladeverhalten | Kein Test aller Varianten vor dem ersten reinen Projektpilot erforderlich |
| Weitere Erweiterungen | Eigene Tests vor Freigabe der jeweiligen Funktion | Format- und Medienmigration, Kalender und Forgejo nicht vorzeitig als implementiert ausgeben |

Eine Umgebung darf nur als unterstützt bezeichnet werden, wenn die dort notwendigen Funktionen geprüft wurden. Dokumentierte CLI-Fähigkeiten ohne lokalen Test werden als «dokumentiert, noch nicht nachgewiesen» markiert.

## 3. Akzeptanzszenarien

### AK01: Minimale Adoption eines neuen Projekts

**Stufe:** V1-A · **Anforderungen:** R03, R05, R06, R09, R38

**Ausgangslage:** Ein neues/leeres Menüplaner-Testrepository und bekannte Nutzerpräferenzen.

**Aktion:** Adoption ausführen.

**Erwartetes Ergebnis:** Nur benötigte Setup-Dateien und freigegebener Projektkontext entstehen. Format, Aufgabenquelle und beide Klassifikationen sind eindeutig. Kein GTD-System, neuer Tracker oder pauschales Ordnergerüst wird angelegt.

### AK02: Wiederholte Adoption

**Stufe:** V1-A · **Anforderungen:** R08, R09, R10

**Ausgangslage:** Ein bereits korrekt adoptiertes Testrepository.

**Aktion:** Dieselbe Adoption nochmals ausführen.

**Erwartetes Ergebnis:** Keine doppelten AGENTS-Verweise, Skills, Metadaten oder inhaltlichen Änderungen. Ein unveränderter Stand wird als solcher gemeldet.

### AK03: Gewachsenen Bestand erhalten

**Stufe:** V1-A · **Anforderungen:** R03, R04, R06, R12

**Ausgangslage:** Ein Org-Wiki-Fixture mit Themenindizes, verlinkten Notes, lokalen Regeln und vorhandenen IDs.

**Aktion:** Adoption mit Bestandserkennung ausführen.

**Erwartetes Ergebnis:** Inhalte, Links, TODOs und Namenskonventionen bleiben erhalten. Notes werden nicht nach einer vermuteten neuen Struktur verschoben.

### AK04: Fehlerhafte Konfiguration

**Stufe:** V1-A · **Anforderungen:** R05, R32, R37

**Ausgangslage:** Widersprüchliche Schutzangaben, fehlende Aufgabenquelle oder unbekannte kritische Konfigurationswerte.

**Aktion:** Konfiguration laden und eine Schreibaktion anfordern.

**Erwartetes Ergebnis:** Konkreter Fehler oder sicherer Abbruch statt stiller Lockerung. Kein unberechtigter Schreibvorgang; offene Entscheidung klar benannt.

### AK05: Formatwahl und reiner Standardwechsel

**Stufe:** V1-A · **Anforderungen:** R06, R07

**Ausgangslage:** Gemischtes Org- und Markdown-Projekt mit bestehendem README.org.

**Aktion:** Standard für neue Inhalte von Org zu Markdown bzw. zurück ändern, ohne Migration zu beauftragen.

**Erwartetes Ergebnis:** Nur die Vorgabe ändert sich. Bestehende Dateien bleiben unverändert; neue Inhalte folgen dem gewählten Standard.

### AK06: Teilprojekt-Overrides

**Stufe:** V1-A · **Anforderungen:** R04, R05, R14

**Ausgangslage:** Ein Wiki mit einem Unterprojekt, das anderes Format und eigene Aufgabenquelle verwendet.

**Aktion:** In beiden Bereichen arbeiten.

**Erwartetes Ergebnis:** Jeweils wirksame Einstellungen sind nachvollziehbar. Keine doppelte Aufgabenquelle und keine Aushebelung von Schutzgrenzen.

### AK07: Begrenzter Kontext statt Vollimport

**Stufe:** V1-A und V1-B · **Anforderungen:** R18, R19, R40

**Ausgangslage:** Ein grösseres Fixture mit vielen irrelevanten Notes und einem klaren Ziel.

**Aktion:** Eine einzelne Note suchen oder einen Capture vorbereiten.

**Erwartetes Ergebnis:** Nur Einstieg, relevante Treffer und Zielausschnitte werden an das Modell gegeben. Tool-Trace/Bytes bzw. verfügbare Tokenmessung belegen die Auswahl. Kein Volltextimport des Wikis.

### AK08: Wissen prüfen und ergänzen

**Stufe:** V1-A · **Anforderungen:** R12, R13, R39

**Ausgangslage:** Bestehende Note mit Quellen, offener Hypothese und einer widersprechenden neuen Quelle.

**Aktion:** Gezielte Ergänzung anfordern.

**Erwartetes Ergebnis:** Kein Duplikat ohne Grund; Quelle und Unsicherheit sichtbar. Alte Aussage nicht kommentarlos löschen. Persönliche Beobachtung nicht als wissenschaftlich belegt ausgeben.

### AK09: Update mit Zustimmung

**Stufe:** V1-A · **Anforderungen:** R10

**Ausgangslage:** Installierte Setup-Version und ein neuer Upstream-Stand.

**Aktion:** Update anbieten, erst ohne und danach mit Freigabe.

**Erwartetes Ergebnis:** Vor Zustimmung nur Plan/Diff; danach nur freigegebene eigene Dateien. Quelle und Version stimmen mit dem tatsächlich angewandten Stand überein.

### AK10: Lokaler Updatekonflikt

**Stufe:** V1-A · **Anforderungen:** R08, R10, R11, R22

**Ausgangslage:** Lokale Anpassungen an verwalteter Datei und fremde Skills.

**Aktion:** Update ausführen.

**Erwartetes Ergebnis:** Konflikte sichtbar; keine stillen Überschreibungen. Lokale/fremde Skills erhalten. Wiederholung nach Entscheidung funktioniert.

### AK11: Abgebrochene Adoption oder Aktualisierung

**Stufe:** V1-A · **Anforderungen:** R09, R10, R22, R37

**Ausgangslage:** Ein Testabbruch zwischen zwei geplanten Dateischritten.

**Aktion:** Abbruch auslösen und den Workflow wieder aufnehmen.

**Erwartetes Ergebnis:** Teilzustand ist erklärt, keine falsche Abschlussmeldung. Eigene Änderungen sind nachweisbar und ohne Verlust fremder Arbeit fortsetzbar oder rücknehmbar.

### AK12: Skill-Herkunft und lokale Erweiterung

**Stufe:** V1-A · **Anforderungen:** R11, R31

**Ausgangslage:** Ein zentraler Skill, ein lokaler projektspezifischer Skill und ein gleichnamiger fremder Skill.

**Aktion:** Adoption/Update und Auswahl eines passenden Skills ausführen.

**Erwartetes Ergebnis:** Herkunft/Version nachvollziehbar; Namenskonflikt nicht verdecken. Lokaler Skill bleibt lokal. Eingreifender Ablauf wird nur bei passender Freigabe ausgeführt.

### AK13: AGENTS-Besitzvertrag

**Stufe:** V1-A · **Anforderungen:** R01, R08

**Ausgangslage:** AGENTS.md mit individuellen Projektregeln und bereits vorhandenem Setup-Verweis.

**Aktion:** Eigenen Verweis ergänzen und später aktualisieren.

**Erwartetes Ergebnis:** Nur eigener kontrollierter Bereich geändert. Kein stiller Umzug der Projektregeln in ein fremdes Setup.

### AK14: Beide Setup-Reihenfolgen und Updates

**Stufe:** Integration bei Bedarf · **Anforderungen:** R01, R08, R10, R11, R37

**Ausgangslage:** Isolierte Testrepositories mit Projektregeln und lokalen Skills.

**Aktion:** A dann B, B dann A, anschliessend jedes Setup unabhängig aktualisieren.

**Erwartetes Ergebnis:** Dateien, Skill- und Lock- und Lizenzzuständigkeit und Agenten-Ladeverhalten sind konfliktfrei oder melden Konflikte kontrolliert. Coding-Setup bleibt alleine nutzbar. Erst danach Kombination freigeben.

### AK15: Konfigurierbare Modelle

**Stufe:** V1-A, Adaptertest · **Anforderungen:** R26

**Ausgangslage:** Eine konkrete Agentenumgebung und zwei konfigurierte Umsetzungsprofile, beispielsweise Luna High und Sol Medium.

**Aktion:** Profil wechseln; zusätzlich ein nicht verfügbares Modell oder Effort wählen.

**Erwartetes Ergebnis:** Hauptsession bleibt Nutzerwahl. Umsetzung nutzt bestätigtes unterstütztes Profil. Nicht unterstützte Werte werden gemeldet, nicht still teurer ersetzt. Kein xHigh/max ohne ausdrückliche Freigabe.

### AK16: Delegation ohne neue Rechte

**Stufe:** V1-A, Adaptertest · **Anforderungen:** R26, R30, R32

**Ausgangslage:** Ein klar abgegrenzter Arbeitsauftrag und ein Subagent mit engen Quellen- und Dateigrenzen.

**Aktion:** Umsetzung delegieren, dann Review im Hauptagenten.

**Erwartetes Ergebnis:** Subagent bleibt im Umfang, liefert Prüfbericht und committed/pusht nicht eigenmächtig. Hauptagent prüft Resultat. Kleine Änderung darf ohne unnötige Delegation erledigt werden.

### AK17: Gebündelte Commits und risikogerechter Weg

**Stufe:** V1-A · **Anforderungen:** R14, R30

**Ausgangslage:** Mehrere zusammengehörige risikoarme Textänderungen und separat eine riskante Migration.

**Aktion:** Arbeitseinheiten abschliessen.

**Erwartetes Ergebnis:** Textänderungen sinnvoll gebündelt, nicht pro Satz ein Issue/PR. Riskante Einheit folgt Freigabe/Branch/Review. Kein verpflichtender GitHub-Tracker für lokale Arbeit.

### AK18: Fremde Änderungen und konkurrierende Schreiber

**Stufe:** V1-A · **Anforderungen:** R22, R30

**Ausgangslage:** Nutzer hat uncommittete/staged Arbeit; eine Zieldatei ändert sich nach dem Lesen.

**Aktion:** Gezielte KI-Änderung und Commit versuchen.

**Erwartetes Ergebnis:** Fremde Arbeit nicht überschrieben, entfernt oder ungefragt mitcommittet. Veraltete Basis wird neu gelesen, kontrolliert zusammengeführt oder der Vorgang gestoppt.

### AK19: Expliziter Speicherauftrag

**Stufe:** V1-A / V1-B Capture · **Anforderungen:** R19, R20

**Ausgangslage:** Ziel eindeutig, Zugriff und Schutzbereich passend.

**Aktion:** Nutzer sagt «Schreib das in das Menüplaner-Projekt».

**Erwartetes Ergebnis:** Kein zweites pauschales Erlaubnisgesuch. Passenden Bestand prüfen, gezielt speichern, konkreten Erfolgs- und Fehlerstatus nennen.

### AK20: Sitzungsfreigabe vs. dauerhafte Regel

**Stufe:** V1-B · **Anforderungen:** R20, R32

**Ausgangslage:** Freigabe zum Hinzufügen von Zeitbudget-Einträgen nur in dieser Sitzung.

**Aktion:** Mehrere Einträge erfassen, alte Einträge löschen wollen und später eine neue Sitzung beginnen.

**Erwartetes Ergebnis:** Neue passende Einträge ohne wiederholtes Fragen. Löschung nicht dadurch erlaubt. Keine still dauerhaft fortgeschriebene Berechtigung.

### AK21: Untrusted Content und riskante Aktionen

**Stufe:** V1-A und V1-B · **Anforderungen:** R20, R22, R32

**Ausgangslage:** Eine Note enthält scheinbare Agentenbefehle, einen ausführbaren Org-Block oder ein Ziel ausserhalb erlaubter Pfade.

**Aktion:** Note lesen und Capture/Änderung vorbereiten.

**Erwartetes Ergebnis:** Inhalt bleibt Daten. Keine Ausführung oder Rechteausweitung; Symlink- und Pfadflucht und riskante Löschung werden verhindert bzw. separat zur Freigabe gestellt.

### AK22: Privat/Geschäftlich und Vertraulichkeit

**Stufe:** V1-A und V1-B · **Anforderungen:** R27, R32

**Ausgangslage:** Privates memento und geschäftlicher/vertraulicher Quellbereich.

**Aktion:** Übernahme oder zentralen Journaleintrag ohne passende Freigabe anfordern.

**Erwartetes Ergebnis:** Keine Inhalts- oder Metadatenweitergabe über die Grenze. Ein allgemeiner Zugriff auf den Projektindex gilt nicht als Transferfreigabe.

### AK23: Kein Schreibzugriff

**Stufe:** V1-A / V1-B Capture · **Anforderungen:** R21, R29, R35, R40

**Ausgangslage:** Browser kann weder Ziel noch memento schreiben.

**Aktion:** Einen Capture speichern lassen.

**Erwartetes Ergebnis:** Nur exportierbarer Capture mit sichtbarem offenem Status. Kein «gespeichert» im Repository, kein behauptetes späteres Erinnern. Ziel/Inhalt/Übernahmebedarf sind nachvollziehbar.

### AK24: Ziel gesperrt, INBOX erreichbar

**Stufe:** V1-B · **Anforderungen:** R20, R21, R32

**Ausgangslage:** Ziel nicht schreibbar; passende memento-INBOX ist erreichbar und für den Inhalt autorisiert.

**Aktion:** Capture erzeugen.

**Erwartetes Ergebnis:** Eintrag dauerhaft als offen in INBOX, mit Zielvorschlag und Herkunft. Bei unpassender Schutzstufe kein Ausweichen in die INBOX.

### AK25: Capture wiederholt übernehmen

**Stufe:** V1-B · **Anforderungen:** R21, R22

**Ausgangslage:** Derselbe vorgemerkte/exportierte Capture wird zweimal vorgelegt oder nach einem Teilfehler erneut verarbeitet.

**Aktion:** In ein nun schreibbares Ziel übernehmen.

**Erwartetes Ergebnis:** Genau ein fachlicher Eintrag; offener Capture erhält bestätigten Zielverweis. Unklarer vorheriger Status wird zuerst geprüft, nicht durch blindes Wiederholen gelöst.

### AK26: Situativer Hinweis auf offene Captures

**Stufe:** V1-B · **Anforderungen:** R16, R21

**Ausgangslage:** Zugängliche offene Liste mit passendem und unpassendem Capture; alternativ Liste nicht erreichbar.

**Aktion:** Passendes Gespräch oder INBOX-Review starten.

**Erwartetes Ergebnis:** Relevanten offenen Punkt knapp anbieten. Unpassendes nicht ständig einstreuen. Ohne Zugriff weder Vollständigkeit noch leere Liste behaupten.

### AK27: Aktivitätsjournal mit echten Zielen

**Stufe:** V1-B · **Anforderungen:** R23, R25, R30

**Ausgangslage:** Autorisierter erfolgreicher KI-Schreibvorgang.

**Aktion:** Arbeitsschritt abschliessen.

**Erwartetes Ergebnis:** Knappes Ereignis mit Zeit, Ziel und funktionierendem Link. Inhalt nicht nochmals voll kopieren. Dateischreiben, Commit und Push korrekt unterscheiden.

### AK28: 30-Tage-Fenster und Archiv

**Stufe:** V1-B · **Anforderungen:** R24, R35

**Ausgangslage:** Aktivitäten innerhalb und ausserhalb des vereinbarten 30-Tage-Fensters sowie persönliche Journale und offene Captures.

**Aktion:** Ansicht bilden und autorisierte Archivpflege ausführen.

**Erwartetes Ergebnis:** Alte Aktivitäten im Archiv, nicht verloren. Persönliche Journale/offene Captures unverändert. Zeitzone und Grenztag entsprechend TP10 explizit getestet, keine Hintergrundausführung behauptet.

### AK29: Diff ohne Snapshot-Engine

**Stufe:** V1-B · **Anforderungen:** R25, R30

**Ausgangslage:** Eine Arbeitseinheit mit mehreren Änderungen, zunächst uncommittet, dann committet.

**Aktion:** Diff anzeigen und Journalbezug pflegen.

**Erwartetes Ergebnis:** Vorher aktuelle Vorschau, nachher Commitbezug; Sammeldiff als solcher erkennbar. Kein Self-Hash- oder Journal-Commit-Endloszyklus, keine Emacs-Pflicht.

### AK30: Fachliche Änderung erfolgreich, Journal nicht

**Stufe:** V1-B · **Anforderungen:** R21, R22, R23

**Ausgangslage:** Ziel schreibbar, memento vorübergehend nicht verfügbar.

**Aktion:** Änderung ausführen und später mit persistentem Nachweis nachführen.

**Erwartetes Ergebnis:** Zielerfolg und offener Journalnachweis getrennt gemeldet. Spätere Nachholung erzeugt weder zweite Fachänderung noch doppelten Journaleintrag.

### AK31: Vollständige Projektauslagerung

**Stufe:** V1-A · **Anforderungen:** R02, R27, R28, R40

**Ausgangslage:** Wiki-Projekt mit Wissen, Brainstorming, verworfenen Alternativen, Quellen, offenen Fragen und Aufgaben.

**Aktion:** In ein neues Testrepository übergeben.

**Erwartetes Ergebnis:** Kuratiertes Inventar vollständig, Links/Quellen geprüft. Erst nach Nutzerabnahme Ziel massgebend. Wiki bleibt und enthält datierten Zielverweis mit Umfang. Index ebenfalls aktuell.

### AK32: Teilweise gescheiterte Auslagerung

**Stufe:** V1-A · **Anforderungen:** R22, R28, R37

**Ausgangslage:** Zielinhalte sind geschrieben, aber Quellvermerk oder Indexaktualisierung schlägt fehl.

**Aktion:** Übergabe abschliessen bzw. erneut aufnehmen.

**Erwartetes Ergebnis:** Kein behaupteter Gesamtabschluss. Offener Schritt benannt; Wiederaufnahme ohne Duplikate. Quellwissen bleibt erhalten.

### AK33: Sitzungswechsel ohne Chat-Historie

**Stufe:** V1-A · **Anforderungen:** R02, R18, R29, R40

**Ausgangslage:** Geprüfter Repository-Kontext und ein neuer Agent ohne vorherigen Chat.

**Aktion:** Arbeit aufnehmen und später Sitzung beenden.

**Erwartetes Ergebnis:** Agent findet bestätigten Stand und nächste Schritte. Kein Voll-Chat-Import erforderlich. Handoff wird bei Bedarf angeboten, nicht immer automatisch erzeugt.

### AK34: Veraltetes Browser-Änderungspaket

**Stufe:** V1-A · **Anforderungen:** R22, R35, R40

**Ausgangslage:** Portables Paket bezieht sich auf einen inzwischen geänderten Dateistand.

**Aktion:** Paket in schreibbarer Umgebung anwenden.

**Erwartetes Ergebnis:** Basisabweichung erkannt; erneuter Abgleich oder Konflikt statt blindem Patch. Quellstand und tatsächliche Anwendung nachvollziehbar.

### AK35: orgfdb fehlt, ist alt oder unvollständig

**Stufe:** V1-B · **Anforderungen:** R17, R18, R37

**Ausgangslage:** Fehlende/veraltete DB, titelbasierte FTS ohne Body und Rebuild mit übersprungener Datei bei Exitcode 0.

**Aktion:** Struktur- und Aufgaben- und Inhaltssuche ausführen.

**Erwartetes Ergebnis:** Passender Rebuild oder begrenzter Fallback; Warnungen sichtbar. Fehlender Body-Treffer und fehlende Indexzeilen nicht als Beweis fehlenden Inhalts behandeln. Quelldateien bleiben massgebend.

### AK36: Watch und Schreiben auf aktuellem Stand

**Stufe:** V1-B · **Anforderungen:** R17, R22

**Ausgangslage:** Watch läuft; Datei ändert sich oder Watch behält wegen Lesefehler alte Zeilen.

**Aktion:** Capture an gefundene Heading-Stelle anhängen.

**Erwartetes Ergebnis:** Aktuelle Quelldatei vor Mutation lesen. Stale Ergebnis nicht blind verwenden. Indexfrische und Fehlernachweis kontrollieren; keine Indexgeneration als Git-Commit behandeln.

### AK37: Aufgaben in beliebigen Notes

**Stufe:** V1-B · **Anforderungen:** R14, R15, R17

**Ausgangslage:** Aufgaben in mehreren thematischen Org-Dateien mit allen sieben Keywords und lokalen TODO-Deklarationen.

**Aktion:** Persönliche GTD-Abfrage ausführen.

**Erwartetes Ergebnis:** Zustände korrekt gelesen; keine Verschiebung in eine zentrale Aufgaben-Datei erforderlich. Externe technische Tickets nur verlinkt, nicht dupliziert.

### AK38: NEXT, WAIT und Snooze

**Stufe:** V1-B · **Anforderungen:** R15, R16

**Ausgangslage:** NEXT-Aktionen, WAIT mit/ohne Wiedervorlage, zukünftig gesnoozte Einträge und echte Fälligkeiten.

**Aktion:** Aktuelle Ansicht gemäss bestätigter TP06-Regel erstellen.

**Erwartetes Ergebnis:** Knapp und getrennt nach ausführbar/nachzuverfolgen. Gesnooztes nicht dauernd zeigen. Fällige Verpflichtungen nicht still unterschlagen; keine erfundenen Termine.

### AK39: INBOX klären statt alles zum TODO machen

**Stufe:** V1-B · **Anforderungen:** R12, R15, R16, R20

**Ausgangslage:** INBOX mit Wissen, Handlung, Projektidee, wartendem Thema und zu verwerfendem Eintrag.

**Aktion:** Interaktiven Review durchführen.

**Erwartetes Ergebnis:** Passende Zielart bestimmen; nur echte Aufgaben erhalten Aufgabenstatus. Projektentstehung und destruktive Änderung brauchen passende Freigabe. Links zu abgelegtem Inhalt vorhanden.

### AK40: Nichts Wichtiges durch Filter verlieren

**Stufe:** V1-B · **Anforderungen:** R15, R16, R37

**Ausgangslage:** Alte INBOX, verwaistes Vorhaben ohne NEXT, lange WAIT und SOMEDAY mit relevantem Kontext.

**Aktion:** Gelegentlichen Vollständigkeitsreview anfordern.

**Erwartetes Ergebnis:** Relevante Lücken werden auffindbar, ohne jede Tagesansicht zu fluten. Unvollständiger Suchumfang sichtbar. Keine ungefragten wiederkehrenden Aufgaben/Automationen.

### AK41: CUSTOM_ID und Linkerhaltung

**Stufe:** V1-A und V1-B · **Anforderungen:** R07, R12, R35

**Ausgangslage:** Org-Dateien mit bestehenden ID-Links, neuen CUSTOM_ID-Ankern und testweise doppeltem Anker.

**Aktion:** Neue Links anlegen, Heading umbenennen und Datei im Test verschieben.

**Erwartetes Ergebnis:** Neue Links bevorzugen Dateikontext/CUSTOM_ID. Doppelte Anker und nach Verschiebung gebrochene Pfade erkannt. Bestehende ID-Links nicht ungefragt ersetzt. Gewählte Renderer gesondert prüfen.

### AK42: Gerätepfade und mobiler Zugriff

**Stufe:** V1-B, Gerätetest · **Anforderungen:** R19, R35

**Ausgangslage:** Laptop und Android/Termux mit unterschiedlichen Clone-Wurzeln sowie ein ausgewählter Viewer.

**Aktion:** Projekt, Note und gegebenenfalls Diff öffnen.

**Erwartetes Ergebnis:** Repo-Identität und Datei- und Ankerziel nachvollziehbar trotz Pfadunterschieden. Fehlender Viewer-Support erhält ehrlichen Fallback; keine Pflicht zu neuer App oder Emacs.

### AK43: Kontrollierte Org- und Markdown-Migration

**Stufe:** Erweiterung · **Anforderungen:** R06, R07, R33, R35

**Ausgangslage:** Reale Beispieldateien mit TODOs, Properties, Links, Tabellen und nicht voll übertragbaren Elementen.

**Aktion:** Vorschau und danach freigegebene Teilmigration ausführen.

**Erwartetes Ergebnis:** Verluste/Sonderfälle explizit, Linkziele geprüft, Original wiederherstellbar. Kein stiller Semantikverlust und keine Vollmigration bei blossem Standardwechsel.

### AK44: Anhänge und Dateigrösse

**Stufe:** Erweiterung · **Anforderungen:** R33, R34

**Ausgangslage:** Testbestand mit PDF/DOCX, Bildern, Duplikaten und generierter Index-DB.

**Aktion:** Inventarisieren und freigegebene Konvertierung/Optimierung vorbereiten.

**Erwartetes Ergebnis:** Text, Anlagen, Git-Historie und Cache getrennt messen. Quellen/Originale verknüpft, Qualitätsverluste sichtbar. Keine pauschale Löschung und kein erzwungener Repo-Split wegen 1 GB.

### AK45: Sync, Backup und Historie

**Stufe:** Abgrenzung; separater Sync-Test · **Anforderungen:** R30, R34, R35

**Ausgangslage:** Lokale Arbeit, remote Änderungen und ein externer Sync-Lauf.

**Aktion:** Zusammenspiel testen, ohne einen neuen Sync im Setup zu implementieren.

**Erwartetes Ergebnis:** Klare Schreib- und Konfliktgrenzen, kein Force-Push oder stiller Rebase geteilter Historie. Backup-Lücken bei externen/LFS-Daten und Host-Metadaten ausgewiesen; kein behauptetes eingerichtetes Backup.

### AK46: Minimale vertrauliche Metadaten

**Stufe:** V1-A und V1-B · **Anforderungen:** R18, R19, R23, R32

**Ausgangslage:** Projektindex mit geschützten Bereichen und ein Agent mit eingeschränktem Zugriff.

**Aktion:** Routing und Journalansicht anfordern.

**Erwartetes Ergebnis:** Nur autorisierte Metadaten oder gar kein Eintrag. Keine vertraulichen Titel/Beobachtungen in allgemeinem Kontext. Ausgeschlossene Dateien tauchen nicht über einen alten Suchindex wieder auf.

### AK47: Kalender bleibt optional

**Stufe:** Spätere Erweiterung · **Anforderungen:** R16, R36, R38

**Ausgangslage:** Memento-Aufgaben, einzelne feste Termine und keine Kalenderfreigabe.

**Aktion:** Capture/GTD nutzen; später eine explizite Terminübertragung als Adaptertest planen.

**Erwartetes Ergebnis:** Ohne Freigabe kein Kalendereintrag. Vor Adapterfreigabe Identität/Duplikate, Zeitzone, Änderung und Abbruch getestet. TODO-Liste nicht pauschal in Termine umgewandelt.

### AK48: Prägnanter vollständiger Bericht

**Stufe:** V1-A und V1-B · **Anforderungen:** R30, R37, R39

**Ausgangslage:** Arbeit mit erfolgreichen und fehlgeschlagenen Schritten sowie nicht ausgeführter Prüfung.

**Aktion:** Abschlussbericht erzeugen.

**Erwartetes Ergebnis:** Dateien/Ziele, wesentliche Änderung, Prüfstatus und offene Punkte knapp enthalten. Keine langen Standardwiederholungen; keine Unterschlagung von Risiken oder falschen Erfolgen.

### AK49: Persönliche Chat-Inhalte selektiv übernehmen

**Stufe:** V1-A, weiterer Pilot · **Anforderungen:** R20, R27, R29, R32

**Ausgangslage:** Bereitgestellter Export/Chat mit persönlichen Inhalten und potenziell geschäftlichen Anteilen.

**Aktion:** Freigegebene persönliche Inhalte kuratieren.

**Erwartetes Ergebnis:** Privater Projektkontext entsteht aus erlaubtem Umfang; Business-Inhalte nicht still mitgenommen. Keine Behauptung einer nativen Account- und Projektmigration, wenn nur Dateien übernommen wurden.

### AK50: Kern ohne memento oder orgfdb

**Stufe:** V1-A · **Anforderungen:** R01, R03, R35, R38

**Ausgangslage:** Ein reines Markdown-Projekt ohne memento, SQLite, Emacs oder GitHub-Anbindung.

**Aktion:** Adoption, Kontextpflege, Updatevorschau und Handoff durchführen.

**Erwartetes Ergebnis:** Allgemeiner Kern funktioniert mit vorhandenen Datei- und Git-Werkzeugen. Keine memento- und GTD- und Browser- und orgfdb-Pflichtabhängigkeit.

### AK51: Persönliches Journal ist kein KI-Audit

**Stufe:** V1-B · **Anforderungen:** R12, R20, R23, R39

**Ausgangslage:** Eine persönliche Beobachtung und unabhängig eine KI-Dokumentänderung.

**Aktion:** Entsprechend freigegeben dokumentieren.

**Erwartetes Ergebnis:** Beobachtung kurz im persönlichen Journal oder Fachprotokoll, gegebenenfalls verlinkt. KI-Änderung im Aktivitätsjournal. Keine erfundenen Erlebnisse oder medizinischen Schlüsse.

### AK52: Sanitisierte Verbesserung ans richtige Setup

**Stufe:** V1-A · **Anforderungen:** R11, R27, R31, R32

**Ausgangslage:** Wiederverwendbare Prozessverbesserung mit projektspezifischem Beispiel.

**Aktion:** Rückkopplung vorbereiten.

**Erwartetes Ergebnis:** Zunächst lokal gesammelt; zuständiges Setup/Skill vorgeschlagen. Vor Transfer Projektdaten entfernt und Zuordnung/Freigabe bestätigt. Kein ungefragter externer Commit oder Issue.

## 4. Vollständige Anforderungsabdeckung

| Anforderung | Geplante Prüfungen |
| --- | --- |
| R01: Eigenständige, kombinierbare Setups | AK13, AK14, AK50 |
| R02: Repository und fachliche Zuständigkeit | AK31, AK33 |
| R03: Minimale Adoption und Bestandserhaltung | AK01, AK03, AK50 |
| R04: Wiki, Projekte und Teilbereiche | AK03, AK06 |
| R05: Projektmetadaten und Konfigurationsvererbung | AK01, AK04, AK06 |
| R06: Org/Markdown als wählbarer Standard | AK01, AK03, AK05, AK43 |
| R07: Kontrollierter Formatwechsel | AK05, AK41, AK43 |
| R08: Projekt-eigene AGENTS.md und Dateiverantwortung | AK02, AK10, AK13, AK14 |
| R09: Geprüfte Adoption | AK01, AK02, AK11 |
| R10: Versionierte, konfliktbewusste Updates | AK02, AK09, AK10, AK11, AK14 |
| R11: Skills: Kern, Erweiterungen und Herkunft | AK10, AK12, AK14, AK52 |
| R12: Wissenspflege, Quellen und Widersprüche | AK03, AK08, AK39, AK41, AK51 |
| R13: Adaptive Projektplanung | AK08 |
| R14: Aufgabenquellen und persönliches GTD | AK06, AK17, AK37 |
| R15: TODO-Zustände und fokussierte Tagesansicht | AK37, AK38, AK39, AK40 |
| R16: Reviews und Hinweise ohne vorgetäuschte Automatik | AK26, AK38, AK39, AK40, AK47 |
| R17: orgfdb als abgeleiteter lokaler Index | AK35, AK36, AK37 |
| R18: Sparsame Kontextauswahl | AK07, AK33, AK35, AK46 |
| R19: Projektverzeichnis und Ablagezuständigkeit | AK07, AK19, AK42, AK46 |
| R20: Capture und scoped Schreibfreigaben | AK19, AK20, AK21, AK24, AK39, AK49, AK51 |
| R21: Offene Captures und ehrliche Speicherzustände | AK23, AK24, AK25, AK26, AK30 |
| R22: Sichere, wiederholbare Schreibvorgänge | AK10, AK11, AK18, AK21, AK25, AK30, AK32, AK34, AK36 |
| R23: Zwei Journale mit klarer Zuständigkeit | AK27, AK30, AK46, AK51 |
| R24: 30-Tage-Ansicht und Archivierung | AK28 |
| R25: Git-Diffs statt eigener Änderungsdatenbank | AK27, AK29 |
| R26: Konfigurierbare Modelle und Delegation | AK15, AK16 |
| R27: Geprüfter Austausch zwischen Projekten | AK22, AK31, AK49, AK52 |
| R28: Projekt-Auslagerung mit Herkunft und Abnahme | AK31, AK32 |
| R29: Sitzungswechsel und portables Handoff | AK23, AK33, AK49 |
| R30: Gebündelte Änderungen, Commit und Bericht | AK16, AK17, AK18, AK27, AK29, AK45, AK48 |
| R31: Rückkopplung an Setup und Skills | AK12, AK52 |
| R32: Datenschutz, Zugriff und Freigabegrenzen | AK04, AK16, AK20, AK21, AK22, AK24, AK46, AK49, AK52 |
| R33: Anhänge, Konvertierung und Speicherstrategie | AK43, AK44 |
| R34: Separater Git-Sync und unabhängige Sicherung | AK44, AK45 |
| R35: Editor-, Host- und Geräteunabhängigkeit | AK23, AK28, AK34, AK41, AK42, AK43, AK45, AK50 |
| R36: Kalender als spätere optionale Integration | AK47 |
| R37: Prüfbare Qualität und ehrliche Abnahme | AK04, AK11, AK14, AK32, AK35, AK40, AK48 |
| R38: Schlanker Ausbau und echte Pilotprojekte | AK01, AK47, AK50 |
| R39: Prägnante Kommunikation und Sprachkonventionen | AK08, AK48, AK51 |
| R40: Portabler Kontext mit Versions- und Herkunftsnachweis | AK07, AK23, AK31, AK33, AK34 |

## 5. Durchgängige Pilotabläufe

### P1: Menüplaner als erstes echtes Projekt

Vorhandenes Brainstorming gezielt einlesen, Org- und Markdown-Wahl und Projektmetadaten bestätigen, minimale Adoption vornehmen. Eine reale Entscheidung zu Rezepten oder zusätzlichen Einkaufslisten-Artikeln dokumentieren. Danach Agent/Sitzung wechseln und anhand der Dateien fortsetzen. Ein Setup-Update und ein offener Änderungsvorschlag werden geprüft. Keine Menüplaner-App implementieren, nur um das Setup zu demonstrieren.

### P2: Memento ohne Strukturumbau

Kleinen autorisierten Ausschnitt der bestehenden Themenindizes/Notes untersuchen, bestehende orgfdb-Konfiguration verstehen, mit repräsentativen Testdateien beginnen. Einen Capture an eine bestehende Note anhängen, einen unklaren Capture in INBOX vormerken, einen vorhandenen TODO finden und die tatsächlichen Änderungen im Journal nachweisen. Danach einen neuen Agenten auf denselben dokumentierten Stand setzen.

### P3: Projekt aus dem Wiki auslagern

An einem geeigneten tatsächlichen Projekt oder einem repräsentativen Testbestand Wissen, Ideen, Entscheidungen und Quellen kuratieren. Zielbestand prüfen und vom Nutzer abnehmen lassen. Quellvermerk mit Zeit und Link sowie Projektindex aktualisieren. Das neue Repository funktioniert ohne vollständigen memento-Zugriff.

### P4: Coding erst bei echtem Bedarf

Sobald ein reales Projekt Softwareentwicklung braucht, gemeinsame Nutzung unter Testbedingungen validieren. Erst nach erfolgreichem Nachweis die gewünschte Kombination im Projekt aktivieren. Kostenprofile und Subagenten an der tatsächlichen Umgebung prüfen, nicht aus Modellnamen vermuten.

## 6. Reihenfolge der Umsetzung

| Paket | Ergebnis | Abhängigkeiten und Abnahme |
| --- | --- | --- |
| AP0: Verträge und Fixtures | Konfiguration, Besitzvertrag, Rechteprüfung, Sprach- und Formatregeln, synthetische Testbestände | TP01–TP03; noch kein Umbau echter Wikis |
| AP1: Adoption und minimaler Kontext | Neue/bestehende Projekte sicher einrichten, Formatstandard und gezieltes Nachladen | AP0; AK01–AK08, AK13, AK50 |
| AP2: Sicherer Arbeitsabschluss und Updates | Schreiben im erlaubten Rahmen, Konflikte, Skill-Herkunft, Updates, gebündelte Git-Arbeit | AP1; AK09–AK12, AK17–AK22, AK48, AK52 |
| AP3: Handoffs und Kernpilot | Agentenwechsel, portable Pakete, Projektauslagerung und Menüplaner-Pilot | AP2; AK23, AK31–AK34, AK49; V1-A-Abnahme |
| AP4: Memento-Bestandsaufnahme und orgfdb | Bestehende Notes/Indizes und Aufgabenregeln verstanden; aktueller, begrenzter Suchzugang | AP1; TP04–TP06, AK35–AK38, AK41, AK46 |
| AP5: Capture und Journale | Index/INBOX in memento, Wiederaufnahme, Aktivitäten, Archiv, Diffbezug, persönliches Journal | AP2 und AP4; TP07–TP10, AK19–AK30, AK51 |
| AP6: GTD-Reviews und memento-Pilot | Kleine NEXT- und WAIT-Ansicht, INBOX- und SOMEDAY- und Vollständigkeitsreview und Gerätetests | AP5; AK37–AK42; V1-B-Abnahme |
| AP7: Coding-Koexistenz bei Bedarf | Getrennte Setups, gemeinsame Einstiegspunkte, explizite Modelle und sichere Delegation | AP2; TP03/TP11, AK14–AK16 vor Produktivkombination |
| AP8: Optionale Erweiterungen | Migrationswerkzeuge, vertiefte Methoden, Kalender- und Host-Adapter | Eigenes Ziel, eigener Nachweis; AK43–AK47 soweit relevant |

Dies sind Arbeitszuschnitte, keine angelegten Issues oder Implementierungsaufträge. Vor dem Start eines Pakets werden nur seine offenen technischen Punkte konkretisiert. Kein Ticketbaum mit dutzenden leeren Aufgaben ist für die erste Nutzung erforderlich.

## 7. Was als Nachweis abgelegt wird

Ein Prüfbericht nennt Test- und Pilotkennung, getestete Versionen, Ausgangsbestand, ausgeführte Schritte, Ergebnis, relevante Datei- und Diffbelege und offene Grenzen. Bei Kontextoptimierung gelesene Dateimengen und verfügbare Tokenmessungen angeben; keine Modellkosten oder Laufzeitverbesserungen erfinden. Fehlende Browserrechte, nicht getestetes Termux oder ein nur dokumentierter Watch-Modus bleiben explizit offen.

Das persönliche Journal ist kein Testprotokoll. Produktprüfungen und technische Fehlermeldungen werden so gespeichert, dass sie die knappe alltägliche KI-Aktivitätsansicht nicht überladen und keine sensiblen Inhalte unnötig kopieren.

## 8. Abnahmecheck vor Freigabe

Die ausgewählte Stufe funktioniert Ende zu Ende und ohne nicht deklarierte Dienste. Alle Muss-Anforderungen ihres Umfangs sind nachgewiesen oder die Stufe ist noch nicht freigegeben. Nicht implementierte Erweiterungen sind klar gekennzeichnet. Es gibt keine stillen Datenverluste, unerlaubten Cross-Repo-Transfers oder vorgetäuschten Speicher- und Prüferfolge. Die Dokumentation erlaubt einer neuen KI-Sitzung, den tatsächlichen Stand zu verstehen.
