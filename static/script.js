const baseUrl = ''
const downloadUrls = {}
function toggle(element) {
    let ele = document.getElementById(element);
    ele.classList.toggle('visually-hidden')
}

function get(id) {
    return document.getElementById(id).value
}

function generate() {
    toggle('genBtn')
    toggle('inprogress')
    let query = `${baseUrl}/api/generate/${get('projectField')}?name=${get('nameField')}&class=${get('classField')}&section=${get('sectionField')}`
    let request = new XMLHttpRequest
    request.open('get', query)
    setTimeout(()=> {
        request.send()}, 1)

    request.onload = function() {
        if (request.status != 200) {
            toggle('inprogress')
            toggle('error')
            setTimeout(() => {
                toggle('error')}, 5000)
            toggle('genBtn')
        } else {
            let response= JSON.parse(request.responseText)
            downloadUrls['data'] = response['urls']
            downloadUrls['template'] = response['data']
            console.log(downloadUrls)
            toggle('inprogress')
            toggle('success')
        }

    }}

function downloadMultiple(){
  toggle('directBtn')
  toggle('emailBtn')
  toggle('succText')
  toggle('successList')
  for (var url in downloadUrls["data"]) {
    let furl = baseUrl + '/' + downloadUrls["data"][url]
    let a = document.createElement('a')
    a.href = furl
    a.download = downloadUrls["data"][url]
    a.innerHTML = parseInt(url) + 1
    a.classList.add('btn')
    a.classList.add('btn-success')
    a.classList.add('m-1')
    a.setAttribute('onClick','remove(this)')
    let list = document.getElementById('successList')
    list.appendChild(a)
  
  }
}

function sendByEmail(){
  toggle('emailAsk')
  toggle('success')
}

function sendEmail(){
  let email = new XMLHttpRequest
  email.open('get',baseUrl+ `/api/email?toemail=${document.getElementById('emailField').value}&name=${downloadUrls['template']['name']}&template=${downloadUrls['template']['templateId']}&file=${downloadUrls['template']['file']}`)
  email.send()
  toggle('emailAsk')
  toggle('inprogress')
  email.onload = function(){
    if (email.status != 200){
      toggle('inprogress')
      toggle('emailError')
    }else{
      toggle('inprogress')
      toggle('emailDone')
    }
  }
  
}

function remove(ele){
  if (document.getElementById('successList').childElementCount == 1){
    let doc = document.getElementById('succText')
    doc.innerHTML = 'Thank you for using guruji. The site will refresh shortly'
    setTimeout(()=> {location.reload()},1000)
  }
  let element = ele
  element.remove()
}
