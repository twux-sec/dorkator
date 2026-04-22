# Dorkator Report — `example.com`

- **Generated:** 2026-04-22 13:17:30
- **Total dorks:** 45

> Legal notice: only run against domains you own or are authorized to assess.


## Credentials & Secrets

### `[CRITICAL]` API keys / tokens

```
site:example.com (intext:"api_key" OR intext:"api_token" OR intext:"access_token" OR intext:"bearer ")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22api_key%22+OR+intext%3A%22api_token%22+OR+intext%3A%22access_token%22+OR+intext%3A%22bearer+%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22api_key%22+OR+intext%3A%22api_token%22+OR+intext%3A%22access_token%22+OR+intext%3A%22bearer+%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22api_key%22+OR+intext%3A%22api_token%22+OR+intext%3A%22access_token%22+OR+intext%3A%22bearer+%22%29)

### `[CRITICAL]` AWS keys

```
site:example.com (intext:"AKIA" OR intext:"aws_secret" OR intext:"aws_access_key")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22AKIA%22+OR+intext%3A%22aws_secret%22+OR+intext%3A%22aws_access_key%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22AKIA%22+OR+intext%3A%22aws_secret%22+OR+intext%3A%22aws_access_key%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22AKIA%22+OR+intext%3A%22aws_secret%22+OR+intext%3A%22aws_access_key%22%29)

### `[CRITICAL]` DB connection strings

```
site:example.com (intext:"jdbc:" OR intext:"mongodb://" OR intext:"postgres://" OR intext:"mysql://")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22jdbc%3A%22+OR+intext%3A%22mongodb%3A%2F%2F%22+OR+intext%3A%22postgres%3A%2F%2F%22+OR+intext%3A%22mysql%3A%2F%2F%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22jdbc%3A%22+OR+intext%3A%22mongodb%3A%2F%2F%22+OR+intext%3A%22postgres%3A%2F%2F%22+OR+intext%3A%22mysql%3A%2F%2F%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22jdbc%3A%22+OR+intext%3A%22mongodb%3A%2F%2F%22+OR+intext%3A%22postgres%3A%2F%2F%22+OR+intext%3A%22mysql%3A%2F%2F%22%29)

### `[CRITICAL]` Environment files

```
site:example.com ext:env
```
[Google](https://www.google.com/search?q=site%3Aexample.com+ext%3Aenv) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+ext%3Aenv) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+ext%3Aenv)

### `[CRITICAL]` Private keys (RSA/SSH/PGP)

```
site:example.com (intext:"BEGIN RSA PRIVATE KEY" OR intext:"BEGIN OPENSSH PRIVATE KEY" OR intext:"BEGIN PRIVATE KEY" OR intext:"BEGIN PGP PRIVATE")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22BEGIN+RSA+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+OPENSSH+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PGP+PRIVATE%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22BEGIN+RSA+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+OPENSSH+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PGP+PRIVATE%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22BEGIN+RSA+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+OPENSSH+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PRIVATE+KEY%22+OR+intext%3A%22BEGIN+PGP+PRIVATE%22%29)


## Exposed Documents

### `[CRITICAL]` SQL dumps

```
site:example.com filetype:sql
```
[Google](https://www.google.com/search?q=site%3Aexample.com+filetype%3Asql) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+filetype%3Asql) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+filetype%3Asql)


## External Leaks

### `[CRITICAL]` GitHub - secrets

```
site:github.com "example.com" (password OR api_key OR token OR secret)
```
[Google](https://www.google.com/search?q=site%3Agithub.com+%22example.com%22+%28password+OR+api_key+OR+token+OR+secret%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Agithub.com+%22example.com%22+%28password+OR+api_key+OR+token+OR+secret%29) · [Bing](https://www.bing.com/search?q=site%3Agithub.com+%22example.com%22+%28password+OR+api_key+OR+token+OR+secret%29)


## Technical Exposure

### `[CRITICAL]` Config files

```
site:example.com (ext:htaccess OR ext:conf OR ext:config OR ext:ini OR ext:yaml OR ext:yml)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28ext%3Ahtaccess+OR+ext%3Aconf+OR+ext%3Aconfig+OR+ext%3Aini+OR+ext%3Ayaml+OR+ext%3Ayml%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28ext%3Ahtaccess+OR+ext%3Aconf+OR+ext%3Aconfig+OR+ext%3Aini+OR+ext%3Ayaml+OR+ext%3Ayml%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28ext%3Ahtaccess+OR+ext%3Aconf+OR+ext%3Aconfig+OR+ext%3Aini+OR+ext%3Ayaml+OR+ext%3Ayml%29)

### `[CRITICAL]` Exposed DB admin interfaces

```
site:example.com (inurl:phpmyadmin OR inurl:adminer OR inurl:pgadmin)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Aphpmyadmin+OR+inurl%3Aadminer+OR+inurl%3Apgadmin%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Aphpmyadmin+OR+inurl%3Aadminer+OR+inurl%3Apgadmin%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Aphpmyadmin+OR+inurl%3Aadminer+OR+inurl%3Apgadmin%29)

### `[CRITICAL]` Version control leaks (.git/.svn/.env)

```
site:example.com (inurl:".git" OR inurl:".svn" OR inurl:".env")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3A%22.git%22+OR+inurl%3A%22.svn%22+OR+inurl%3A%22.env%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3A%22.git%22+OR+inurl%3A%22.svn%22+OR+inurl%3A%22.env%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3A%22.git%22+OR+inurl%3A%22.svn%22+OR+inurl%3A%22.env%22%29)

### `[CRITICAL]` phpinfo() exposure

```
site:example.com ext:php intitle:phpinfo "PHP Version"
```
[Google](https://www.google.com/search?q=site%3Aexample.com+ext%3Aphp+intitle%3Aphpinfo+%22PHP+Version%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+ext%3Aphp+intitle%3Aphpinfo+%22PHP+Version%22) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+ext%3Aphp+intitle%3Aphpinfo+%22PHP+Version%22)


## Credentials & Secrets

### `[HIGH]` Passwords in text

```
site:example.com (intext:"password" OR intext:"passwd" OR intext:"motdepasse" OR intext:"mot de passe")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22password%22+OR+intext%3A%22passwd%22+OR+intext%3A%22motdepasse%22+OR+intext%3A%22mot+de+passe%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22password%22+OR+intext%3A%22passwd%22+OR+intext%3A%22motdepasse%22+OR+intext%3A%22mot+de+passe%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22password%22+OR+intext%3A%22passwd%22+OR+intext%3A%22motdepasse%22+OR+intext%3A%22mot+de+passe%22%29)


## Exposed Documents

### `[HIGH]` Backup files

```
site:example.com (ext:bak OR ext:backup OR ext:old OR ext:save OR ext:swp)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28ext%3Abak+OR+ext%3Abackup+OR+ext%3Aold+OR+ext%3Asave+OR+ext%3Aswp%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28ext%3Abak+OR+ext%3Abackup+OR+ext%3Aold+OR+ext%3Asave+OR+ext%3Aswp%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28ext%3Abak+OR+ext%3Abackup+OR+ext%3Aold+OR+ext%3Asave+OR+ext%3Aswp%29)

### `[HIGH]` PDFs flagged confidential

```
site:example.com filetype:pdf (intext:confidential OR intext:confidentiel OR intext:internal OR intext:"do not distribute" OR intext:"usage interne")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+filetype%3Apdf+%28intext%3Aconfidential+OR+intext%3Aconfidentiel+OR+intext%3Ainternal+OR+intext%3A%22do+not+distribute%22+OR+intext%3A%22usage+interne%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+filetype%3Apdf+%28intext%3Aconfidential+OR+intext%3Aconfidentiel+OR+intext%3Ainternal+OR+intext%3A%22do+not+distribute%22+OR+intext%3A%22usage+interne%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+filetype%3Apdf+%28intext%3Aconfidential+OR+intext%3Aconfidentiel+OR+intext%3Ainternal+OR+intext%3A%22do+not+distribute%22+OR+intext%3A%22usage+interne%22%29)

### `[HIGH]` Spreadsheets (XLS/XLSX/CSV)

```
site:example.com (filetype:xls OR filetype:xlsx OR filetype:csv)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28filetype%3Axls+OR+filetype%3Axlsx+OR+filetype%3Acsv%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28filetype%3Axls+OR+filetype%3Axlsx+OR+filetype%3Acsv%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28filetype%3Axls+OR+filetype%3Axlsx+OR+filetype%3Acsv%29)


## External Leaks

### `[HIGH]` Azure blob storage

```
site:blob.core.windows.net "example.com"
```
[Google](https://www.google.com/search?q=site%3Ablob.core.windows.net+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Ablob.core.windows.net+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Ablob.core.windows.net+%22example.com%22)

### `[HIGH]` GitLab mentions

```
site:gitlab.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Agitlab.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Agitlab.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Agitlab.com+%22example.com%22)

### `[HIGH]` Pastebin leaks

```
site:pastebin.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Apastebin.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Apastebin.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Apastebin.com+%22example.com%22)

### `[HIGH]` S3 buckets

```
site:s3.amazonaws.com "example.com"
```
[Google](https://www.google.com/search?q=site%3As3.amazonaws.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3As3.amazonaws.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3As3.amazonaws.com+%22example.com%22)


## Technical Exposure

### `[HIGH]` Admin panels

```
site:example.com (inurl:admin OR inurl:administrator OR inurl:backend OR inurl:dashboard)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Aadmin+OR+inurl%3Aadministrator+OR+inurl%3Abackend+OR+inurl%3Adashboard%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Aadmin+OR+inurl%3Aadministrator+OR+inurl%3Abackend+OR+inurl%3Adashboard%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Aadmin+OR+inurl%3Aadministrator+OR+inurl%3Abackend+OR+inurl%3Adashboard%29)

### `[HIGH]` Apache server-status / server-info

```
site:example.com (inurl:server-status OR inurl:server-info)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Aserver-status+OR+inurl%3Aserver-info%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Aserver-status+OR+inurl%3Aserver-info%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Aserver-status+OR+inurl%3Aserver-info%29)

### `[HIGH]` Open directory listings

```
site:example.com intitle:"index of"
```
[Google](https://www.google.com/search?q=site%3Aexample.com+intitle%3A%22index+of%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+intitle%3A%22index+of%22) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+intitle%3A%22index+of%22)

### `[HIGH]` Verbose error messages

```
site:example.com (intext:"SQL syntax" OR intext:"fatal error" OR intext:"stack trace" OR intext:"warning: include")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22SQL+syntax%22+OR+intext%3A%22fatal+error%22+OR+intext%3A%22stack+trace%22+OR+intext%3A%22warning%3A+include%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22SQL+syntax%22+OR+intext%3A%22fatal+error%22+OR+intext%3A%22stack+trace%22+OR+intext%3A%22warning%3A+include%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22SQL+syntax%22+OR+intext%3A%22fatal+error%22+OR+intext%3A%22stack+trace%22+OR+intext%3A%22warning%3A+include%22%29)


## Exposed Documents

### `[MEDIUM]` PowerPoint presentations

```
site:example.com (filetype:ppt OR filetype:pptx)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28filetype%3Appt+OR+filetype%3Apptx%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28filetype%3Appt+OR+filetype%3Apptx%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28filetype%3Appt+OR+filetype%3Apptx%29)

### `[MEDIUM]` Text / log files

```
site:example.com (filetype:txt OR filetype:log)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28filetype%3Atxt+OR+filetype%3Alog%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28filetype%3Atxt+OR+filetype%3Alog%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28filetype%3Atxt+OR+filetype%3Alog%29)

### `[MEDIUM]` Word documents

```
site:example.com (filetype:doc OR filetype:docx)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28filetype%3Adoc+OR+filetype%3Adocx%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28filetype%3Adoc+OR+filetype%3Adocx%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28filetype%3Adoc+OR+filetype%3Adocx%29)


## External Leaks

### `[MEDIUM]` Public Google Docs

```
site:docs.google.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Adocs.google.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Adocs.google.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Adocs.google.com+%22example.com%22)

### `[MEDIUM]` Public Trello boards

```
site:trello.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Atrello.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Atrello.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Atrello.com+%22example.com%22)


## Identities & Contacts

### `[MEDIUM]` Domain emails (text)

```
site:example.com intext:"@example.com"
```
[Google](https://www.google.com/search?q=site%3Aexample.com+intext%3A%22%40example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+intext%3A%22%40example.com%22) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+intext%3A%22%40example.com%22)

### `[MEDIUM]` Emails in documents

```
site:example.com (filetype:pdf OR filetype:docx OR filetype:xlsx) intext:"@example.com"
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28filetype%3Apdf+OR+filetype%3Adocx+OR+filetype%3Axlsx%29+intext%3A%22%40example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28filetype%3Apdf+OR+filetype%3Adocx+OR+filetype%3Axlsx%29+intext%3A%22%40example.com%22) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28filetype%3Apdf+OR+filetype%3Adocx+OR+filetype%3Axlsx%29+intext%3A%22%40example.com%22)

### `[MEDIUM]` Internal directories

```
site:example.com (inurl:annuaire OR inurl:directory OR inurl:employees)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Aannuaire+OR+inurl%3Adirectory+OR+inurl%3Aemployees%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Aannuaire+OR+inurl%3Adirectory+OR+inurl%3Aemployees%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Aannuaire+OR+inurl%3Adirectory+OR+inurl%3Aemployees%29)


## Subdomains & Assets

### `[MEDIUM]` Dev / staging / preprod

```
site:*.example.com (inurl:dev OR inurl:staging OR inurl:test OR inurl:preprod OR inurl:uat OR inurl:recette)
```
[Google](https://www.google.com/search?q=site%3A%2A.example.com+%28inurl%3Adev+OR+inurl%3Astaging+OR+inurl%3Atest+OR+inurl%3Apreprod+OR+inurl%3Auat+OR+inurl%3Arecette%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3A%2A.example.com+%28inurl%3Adev+OR+inurl%3Astaging+OR+inurl%3Atest+OR+inurl%3Apreprod+OR+inurl%3Auat+OR+inurl%3Arecette%29) · [Bing](https://www.bing.com/search?q=site%3A%2A.example.com+%28inurl%3Adev+OR+inurl%3Astaging+OR+inurl%3Atest+OR+inurl%3Apreprod+OR+inurl%3Auat+OR+inurl%3Arecette%29)

### `[MEDIUM]` Internal-looking paths

```
site:example.com (inurl:internal OR inurl:intranet OR inurl:private)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Ainternal+OR+inurl%3Aintranet+OR+inurl%3Aprivate%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Ainternal+OR+inurl%3Aintranet+OR+inurl%3Aprivate%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Ainternal+OR+inurl%3Aintranet+OR+inurl%3Aprivate%29)


## Technical Exposure

### `[MEDIUM]` Login pages

```
site:example.com (inurl:login OR inurl:signin OR inurl:auth OR intitle:"login")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Alogin+OR+inurl%3Asignin+OR+inurl%3Aauth+OR+intitle%3A%22login%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Alogin+OR+inurl%3Asignin+OR+inurl%3Aauth+OR+intitle%3A%22login%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Alogin+OR+inurl%3Asignin+OR+inurl%3Aauth+OR+intitle%3A%22login%22%29)

### `[MEDIUM]` Swagger / API docs exposed

```
site:example.com (inurl:swagger OR inurl:api-docs OR inurl:redoc OR inurl:graphql)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Aswagger+OR+inurl%3Aapi-docs+OR+inurl%3Aredoc+OR+inurl%3Agraphql%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Aswagger+OR+inurl%3Aapi-docs+OR+inurl%3Aredoc+OR+inurl%3Agraphql%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Aswagger+OR+inurl%3Aapi-docs+OR+inurl%3Aredoc+OR+inurl%3Agraphql%29)

### `[MEDIUM]` WordPress wp-admin / wp-config

```
site:example.com (inurl:wp-admin OR inurl:wp-config OR inurl:wp-content/uploads)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Awp-admin+OR+inurl%3Awp-config+OR+inurl%3Awp-content%2Fuploads%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Awp-admin+OR+inurl%3Awp-config+OR+inurl%3Awp-content%2Fuploads%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Awp-admin+OR+inurl%3Awp-config+OR+inurl%3Awp-content%2Fuploads%29)


## External Leaks

### `[LOW]` StackOverflow mentions

```
site:stackoverflow.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Astackoverflow.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Astackoverflow.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Astackoverflow.com+%22example.com%22)


## Identities & Contacts

### `[LOW]` Contact / team pages

```
site:example.com (inurl:contact OR inurl:team OR inurl:about OR inurl:staff OR inurl:equipe)
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28inurl%3Acontact+OR+inurl%3Ateam+OR+inurl%3Aabout+OR+inurl%3Astaff+OR+inurl%3Aequipe%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28inurl%3Acontact+OR+inurl%3Ateam+OR+inurl%3Aabout+OR+inurl%3Astaff+OR+inurl%3Aequipe%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28inurl%3Acontact+OR+inurl%3Ateam+OR+inurl%3Aabout+OR+inurl%3Astaff+OR+inurl%3Aequipe%29)

### `[LOW]` Phone numbers (FR)

```
site:example.com (intext:"+33" OR intext:"06." OR intext:"07.")
```
[Google](https://www.google.com/search?q=site%3Aexample.com+%28intext%3A%22%2B33%22+OR+intext%3A%2206.%22+OR+intext%3A%2207.%22%29) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aexample.com+%28intext%3A%22%2B33%22+OR+intext%3A%2206.%22+OR+intext%3A%2207.%22%29) · [Bing](https://www.bing.com/search?q=site%3Aexample.com+%28intext%3A%22%2B33%22+OR+intext%3A%2206.%22+OR+intext%3A%2207.%22%29)


## Personnel Intelligence

### `[LOW]` CVs / resumes mentioning target

```
("CV" OR "resume" OR "curriculum vitae") "example.com" filetype:pdf
```
[Google](https://www.google.com/search?q=%28%22CV%22+OR+%22resume%22+OR+%22curriculum+vitae%22%29+%22example.com%22+filetype%3Apdf) · [DuckDuckGo](https://duckduckgo.com/?q=%28%22CV%22+OR+%22resume%22+OR+%22curriculum+vitae%22%29+%22example.com%22+filetype%3Apdf) · [Bing](https://www.bing.com/search?q=%28%22CV%22+OR+%22resume%22+OR+%22curriculum+vitae%22%29+%22example.com%22+filetype%3Apdf)

### `[LOW]` LinkedIn profiles mentioning target

```
site:linkedin.com/in "example.com"
```
[Google](https://www.google.com/search?q=site%3Alinkedin.com%2Fin+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Alinkedin.com%2Fin+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Alinkedin.com%2Fin+%22example.com%22)

### `[LOW]` Viadeo profiles

```
site:viadeo.com "example.com"
```
[Google](https://www.google.com/search?q=site%3Aviadeo.com+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aviadeo.com+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Aviadeo.com+%22example.com%22)


## Subdomains & Assets

### `[LOW]` All subdomains (excl. www)

```
site:*.example.com -site:www.example.com
```
[Google](https://www.google.com/search?q=site%3A%2A.example.com+-site%3Awww.example.com) · [DuckDuckGo](https://duckduckgo.com/?q=site%3A%2A.example.com+-site%3Awww.example.com) · [Bing](https://www.bing.com/search?q=site%3A%2A.example.com+-site%3Awww.example.com)


## External Leaks

### `[INFO]` Archive.org snapshots

```
site:web.archive.org "example.com"
```
[Google](https://www.google.com/search?q=site%3Aweb.archive.org+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=site%3Aweb.archive.org+%22example.com%22) · [Bing](https://www.bing.com/search?q=site%3Aweb.archive.org+%22example.com%22)


## Personnel Intelligence

### `[INFO]` Twitter / X mentions

```
(site:twitter.com OR site:x.com) "example.com"
```
[Google](https://www.google.com/search?q=%28site%3Atwitter.com+OR+site%3Ax.com%29+%22example.com%22) · [DuckDuckGo](https://duckduckgo.com/?q=%28site%3Atwitter.com+OR+site%3Ax.com%29+%22example.com%22) · [Bing](https://www.bing.com/search?q=%28site%3Atwitter.com+OR+site%3Ax.com%29+%22example.com%22)
