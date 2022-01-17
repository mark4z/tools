package main

import (
	"crypto/md5"
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"strings"
	"time"
)

func main() {
	args := flag.Int("t", 100, "t")
	flag.Parse()

	total := *args
	log.Println(total)

	cur := 0

	for i := 0; i < 100; i++ {
		id := "P003756"
		rand.Seed(time.Now().UnixNano())

		point := 50 + rand.Intn(100)

		cur += point
		if cur > total {
			break
		}

		timestamp := time.Now().UnixNano() / 1e6
		md5S := "LianWei!@#XunShangpoint" + strconv.Itoa(point) + "timestamp" + fmt.Sprintf("%d", timestamp) + "userId" + id
		println(md5S)

		data := []byte(md5S)
		has := md5.Sum(data)
		md5str := fmt.Sprintf("%X", has)

		body := map[string]interface{}{}
		body["userId"] = id
		body["point"] = point
		body["timestamp"] = timestamp
		body["token"] = md5str
		marshal, _ := json.Marshal(body)
		println(marshal)

		request, _ := http.NewRequest("POST", "https://ees2022.mucii.com/lianwei/game/point", strings.NewReader(string(marshal)))
		request.Header.Set("content-type", "application/json")
		request.Header.Set("referer", "https://servicewechat.com/wx62cad93ff47d15da/3/page-frame.html")
		request.Header.Set("accept-encoding", "gzip, deflate, br")

		client := &http.Client{}
		do, _ := client.Do(request)
		defer do.Body.Close()

		all, _ := ioutil.ReadAll(do.Body)
		log.Println(point, cur, string(all))

		delay := 30 + int(point/5)
		time.Sleep(time.Duration(delay) * time.Second)
	}

}
