function gotTo(page,parmkey="id",param="") {
    url = "/" + page + "/";
    if ( param !== "")
        url += "?" + paramKey + "=" + param;
    console.log(url);
    location.href = url;
}