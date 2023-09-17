

function customFetchPush(url,payload,headers){
    fetch(url,{
        method:"POST",
        body:JSON.stringify(payload),
        headers:headers
    }).then(response=>response.json())
    .then(data=>{
        // if (data.message == "success"){
        //     window.location.href = "/home"
        // }else{
        //     alert(data.message)
        // }
        return data
    })
    .catch(err=>console.log(err))
}