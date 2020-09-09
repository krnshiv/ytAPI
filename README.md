This is an api designed usiing Django v3.1.1, DjanoRestFramework v3 ,python3.6

YouTubeAPI-v1

->ytAPI module, houses the schema of DB and APIview
---->APIviews the latest published videos under the query('football')
---->DB stores the videoId,titlem,descroption and publishedAt data from the youtubeAPI

->fetch module pings the youtube DATA API every x seconds and store the new (distinct results in the db)

