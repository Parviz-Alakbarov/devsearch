 //Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let alertWrapperall = document.querySelectorAll('.alert')
if (alertWrapperall) {
    for(var i = 0; i<alertWrapperall.length; i++){
        const alertWrapper = alertWrapperall[i];
        const button = alertWrapper.querySelector('.alert__close');
        if (button) {
          button.addEventListener('click', function() {
            alertWrapper.style.display = 'none';
          });
        }
    }
}
