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




### Example User profile json ###
```json
{
  "a00001": {},
  "thisuser": {
    "_t": "xresp",
    "rc": "OK",
    "result": {
      "data": {
        "udate": 1625783523106,
        "_t": "pstfd",
        "cdate": 1625783523106,
        "list": [
          {
            "udate": 1625783523106,
            "_t": "psti",
            "cdate": 1625390731608,
            "receiver_id": "a00001",
            "activity": {
              "cdate": 1625390731608,
              "init_id": "a00001",
              "src_type": "u",
              "src_id": "a00001",
              "action": "likes_pst",
              "tgt_type": "post",
              "tgt_id": "pew6",
              "tgt_oid": "support",
              "pstid": "pew6",
              "uid": "support",
              "_id": "aqbvga"
            },
            "_id": "a00001_aqbvga",
            "action": "likes_pst"
          }
        ],
        "_id": "ufd_a00001"
      },
      "aux": {
        "removed": 1,
        "pinf": null,
        "post": {
          "pew6": {
            "acl": {
              "pub": 4
            },
            "vis": "p",
            "txt": "Welcome to GETTR and start a new journey!",
            "vid_wid": 1920,
            "vid_hgt": 1080,
            "imgs": [
              "group1/getter/2021/07/01/10/cde6a698-a53d-18c5-05a1-4c03eb29013c/a38d12f846dc2834c7ad8846f3e97623.jpg"
            ],
            "meta": [
              {
                "wid": null,
                "hgt": null,
                "meta": {
                  "heads": null
                }
              }
            ],
            "main": "group1/getter/2021/07/01/10/cde6a698-a53d-18c5-05a1-4c03eb29013c/a38d12f846dc2834c7ad8846f3e97623.jpg",
            "_t": "post",
            "uid": "support",
            "cdate": 1625145020469,
            "udate": 1625145020469,
            "_id": "pew6"
          }
        },
        "s_pst": {
          "pew6": {
            "lkbpst": "33383",
            "cm": "150681",
            "shbpst": "2383",
            "vfpst": "47709",
            "vspst": "3029"
          }
        },
        "uinf": {
          "a00001": {
            "udate": "1625390456943",
            "_t": "uinf",
            "_id": "a00001",
            "nickname": "a00001",
            "username": "a00001",
            "ousername": "a00001",
            "dsc": "null",
            "status": "a",
            "cdate": "1625390456941",
            "lang": "en",
            "location": "null",
            "flw": "12",
            "flg": "6",
            "lkspst": "2"
          },
          "support": {
            "udate": "1625531847570",
            "_t": "uinf",
            "_id": "support",
            "nickname": "Support & Help",
            "username": "support",
            "ousername": "support",
            "dsc": "Account of GETTR support team",
            "status": "a",
            "cdate": "1625132755820",
            "lang": "en",
            "infl": 5,
            "ico": "group32/getter/2021/07/01/09/d9afb416-365a-4b26-d286-77e896dcb2b5/e0a628c3ce79d5178af9f033868f9153.jpg",
            "bgimg": "group25/getter/2021/07/02/12/acd80071-ece7-af19-03b6-c864f5a44268/c205b9f9e47b265756c4d07dd9ba8ffc.jpg",
            "location": "NYC, NY",
            "flw": "0",
            "flg": "22091"
          }
        },
        "lks": [],
        "shrs": []
      },
      "serial": "pstfd"
    }
  }
}
```

### Example [aux][post] JSON ###
```json
"######": {
          "acl": {
            "pub": 4
          },
          "vis": "p",
          "txt": "buncha stupid crap some dumdumd said",
          "vid_wid": 1875,
          "vid_hgt": 2343,
          "imgs": [
            "group20/getter/2021/07/07/17/352e93f7-afae-0c75-d633-85cde48a8d95/noway.jpg"
          ],
          "meta": [
            {
              "wid": null,
              "hgt": null,
              "meta": {
                "heads": null
              }
            }
          ],
          "main": "group20/getter/2021/07/07/17/352e93f7-afae-0c75-d633-85cde48a8d95/noway.jpg",
          "htgs": null,
          "utgs": null,
          "_t": "post",
          "uid": "nra",
          "cdate": 1625677743253,
          "udate": 1625677743253,
          "_id": "######"
        }
```          


# Be nice! Dont do mean or destructive things with this info. POC only, for educational, instructional, and entertainment purposes only. Do no harm. #
    
