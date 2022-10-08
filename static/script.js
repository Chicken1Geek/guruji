const baseUrl = ''
let downloadUrl = ''

function toggle(element){
  let ele = document.getElementById(element);
  ele.classList.toggle('visually-hidden')
}

function get(id){
  return document.getElementById(id).value
}

function generate(){
  toggle('genBtn')
  toggle('inprogress')
  let query = `${baseUrl}/api/generate/${get('projectField')}?name=${get('nameField')}&class=${get('classField')}&section=${get('sectionField')}`
  let request = new XMLHttpRequest
  request.open('get',query)
  setTimeout(()=>{request.send()},2000)
  
  request.onload = function(){
    if (request.status != 200){
    toggle('inprogress')
    toggle('error')
    setTimeout(() => {toggle('error')},5000)
    toggle('genBtn')
  }else{
    downloadUrl = `${baseUrl}/${request.responseText}`
    toggle('inprogress')
    toggle('success')
  }
  
}}

function download(){
  window.open(downloadUrl)
  toggle('success')
  toggle('genBtn')
}
