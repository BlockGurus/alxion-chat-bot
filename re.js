// ⁠ https://api.twitter.com/2/tweets/:id/retweeted_by ⁠; // get retweeters of a tweet

// curl --location 'https://api.twitter.com/2/tweets/:id/retweeted_by' \
// --header 'Authorization: Bearer mytoken123••••••'
// 
// {
//     "data": [
//         {
//             "id": "716078211797487616",
//             "name": "davyĸιng",
//             "username": "im_davyking"
//         }
//     ],
//     "meta": {
//         "result_count": 1,
//         "next_token": "7140dibdnow9c7btw4b0pn1kiz13e2bhpk9u8x8dja3ao"
//     }
// }
// ⁠ https://api.twitter.com/2/tweets/:id/liking_users ⁠; // get users who liked a tweet
