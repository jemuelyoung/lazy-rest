;
function input_processing(url, data){
	var self = this, request;
	request = new XMLHttpRequest();
	
	if(url.lastindexof("http://",0) === 0){
		url = "http://" + url;
	}
	
	if(data === null){
		request.open("GET", url, true);
	} else{
		request.open("POST", url, true);
		request.setRequestHeader("Content-type","multipart/form-data");
	}
	
}
