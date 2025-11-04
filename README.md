# ublacklist-generator
I use [uBlacklist](https://github.com/iorate/ublacklist) because it's nice being able to omit certain results from my search, e.g., Pinterest. Pinterest in particular annoys me because you're forced to create an account in order to view results. However, I found that simply adding a rule like `*://*.pinterest.com/*` wasn't sufficient because I would then see results from `pinterest.ie` and other domains.

## How Does it Work?
`generate-blacklist.py` fetches a list of known international domains from this [gist](https://raw.githubusercontent.com/samayo/country-json/refs/heads/master/src/country-by-domain-tld.json). It then takes one or more names, e.g., `alamy` and creates a number of possible domain names, e.g., `alamy.com`, `alamy.net`, `alamy.fr`, etc. Once the list is generated and sorted for all of the specified names, the script checks them for connectivty in batches of 50. There is a progress bar that shows you the domain currently being checked as well as an indicator showing the number of resolved and unresolved domains.

A text file that looks like this is created. From there you simply paste its contents into uBlacklist's configuration panel.
```
*://*.alamy.co/*
*://*.alamy.com.ar/*
*://*.alamy.com.au/*
*://*.alamy.com.br/*
*://*.alamy.com.cc/*
*://*.alamy.com.cn/*
*://*.alamy.com.de/
...
*://*.tiktok.vc/*
*://*.tiktok.vg/*
*://*.tiktok.vn/*
*://*.tiktok.vu/*
```

## Sample Run
I specified eight sites with a total of 3,808 possible domain names. 568 rules were generated in under 20 seconds.
```
% time generate-blacklist.py -d 123rf -d alamy -d dreamstime -d gettyimages -d istockphoto -d pinterest -d shutterstock -d tiktok
Checking tiktok.tn          : 100%|██████████████████████████| 3808/3808 [00:17<00:00, 221.13it/s, fail=3240, ok=568]

Done in 17.29s
568 domains resolved.
uBlacklist file saved to: uBlacklist.txt
generate-blacklist.py -d 123rf -d alamy -d dreamstime -d gettyimages -d  -d  4.93s user 0.97s system 33% cpu 17.707 total
```
