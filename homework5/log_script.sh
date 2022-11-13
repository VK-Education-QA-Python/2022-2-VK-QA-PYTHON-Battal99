#!/bin/bash
#
# Usage: ./log_script access.log
clear

PATH_TO_LOG_FILE=$1


if [ -n "$1" ]
then
	echo "The first argument is $1"
else
	echo "Invalid path"
exit 0
fi

touch result.txt
cat /dev/null > result.txt
result="result.txt"

counts_request=$(cat $PATH_TO_LOG_FILE | wc -l)
echo "$counts_request"
echo "counts request =$counts_request" >>$result

total_requests_by_type=$(cat $PATH_TO_LOG_FILE | awk '{print $6}' | sort | uniq -c)
echo "total_requests_by_type = $total_requests_by_type"
echo "total_requests_by_type = $total_requests_by_type" >>$result

top_server_error=$(cat $PATH_TO_LOG_FILE |awk -F' ' '$9 ~ /^5../' | sort| awk '{print $1}'| uniq -c| sort -nk1| tail -n 5)
echo "top_server_error = $top_server_error"
echo "top_server_error = $top_server_error" >>$result

top_bad_request=$(cat $PATH_TO_LOG_FILE | awk -F' ' '$9 ~ /^4../' | uniq | sort -nk 10 | awk '{print $7, $9, $10, $1}' | tail -n 5)
echo "top_bad_request = $top_bad_request"
echo "top_bad_request = $top_bad_request" >>$result

top_urls=$(cat $PATH_TO_LOG_FILE | awk -F'"' '{print $2}' | awk '{print $2}' | sort | uniq -c | sort -n | tail -n 10)
echo "top_urls = $top_urls"
echo "top urls = $top_urls" >>$result
