# gottr

Uh oh... Someone didnt protect their API very well.

![](https://i.imgur.com/BQxUoNC.gif)

## Road Notes: ##
1. "api.[target].com" is completely plaintext with no auth. (list of endpoints here later)
2. "media.[target].com" is also completely plaintext and requires no auth. The paths for all media can be scraped from user post and reply jsons. 
3. Didnt find a limter for api calls, but safe bet is >0.8sec.
4. Individual posts are stored as a 6 char alphanum under the path "[target].com/post/[6char-hash]. Bruting this path isnt very effective and would probably pop protections (if any exist, lol prob not). Spot checking some random hashes found more than 2/3rd's were empty, so its more efficient to crawl by individual user.
5. Built username lists for 13 accounts with more than 500 followers. Found that service is only incrementing the total followers number. Spot checked individual username list count to displayed follower count is not accurate (probably a lazy redis HINCRBY). Tarball is here: [followers by top usernames](http://mentalburden.com/payloads/followers-by-username.tar.gz)
6. Unique username list was built from the followers of the 13 accounts above. List is in the repo, tarball is here: [unique usernames](http://mentalburden.com/payloads/unique-usernames.tar.gz)
7. For each username: check if length of returnjson[request][data][list] is >= 1, if true write to text files organized by first character of each username.
8. Scrape "media.[target].com" for paths found in the resultant lists from the username check above. Think ill need to get an s3 spun up for that... Or maybe ill just base64 them all and cram them into a burner firebase rtdb. Hmm...

# Be nice! Dont do mean or destructive things with this info. POC only, for educational, instructional, and entertainment purposes only. Do no harm. #
    
