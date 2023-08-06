function sendValue(value) {
  Streamlit.setComponentValue(value)
}

function addRowHTML(image_path, name, id) {

  var html_text = `
    <div class="card swiper-slide">
      <div class="image">
        <div class="image-content">
          <span class="overlay"></span>
          <div class="card-image">
            <img src="{image_path}" alt="" class="card-img">
          </div>
        </div>
      </div>
      <div class="card-content">
        <h2 class="name">{name}</h2>
        <p class="description">PhD in Neuroscience</p>
        <button class="button" id="{id}" onclick="handleClick(this)">View More</button>
      </div>
    </div>
  `;
  html_text = html_text.replace("{image_path}", image_path);
  html_text = html_text.replace("{name}", name);
  html_text = html_text.replace("{id}", name);
  
  document.querySelector('.card-wrapper').insertAdjacentHTML(
    'beforeend',
    html_text     
  )

}

function handleClick(component){
  sendValue(component.id);
}

var first_run = true;

function onRender(event) {

  if (first_run) {
    var {label} = event.detail.args;

    for (var i=0 ; i < label.length ; i++){
      addRowHTML(label[i][0], label[i][1], label[i][1].toLowerCase().replace(" ", "_"));
    }

    first_run = false;
  }

  if (!window.rendered) {
    window.rendered = true
  }
}


Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight(430)
Streamlit.setFrameWidth(704)
