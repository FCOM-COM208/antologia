// Render books
const grid = document.getElementById('grid');
collection.forEach(book => {
    const bookItem = document.createElement('li');
    bookItem.classList.add('book-item', 'small-12', 'medium-6', 'columns');
    bookItem.dataset.groups = JSON.stringify(book.categories);
    bookItem.dataset.dateCreated = book.published;
    bookItem.dataset.title = book.title;

    bookItem.innerHTML = `
    <div class="bk-img">
      <div class="bk-wrapper">
        <div class="bk-book bk-bookdefault">
          <div class="bk-front">
            <div class="bk-cover" style="background-image: url('${book.coverSmall}')"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="item-details">
      <h3 class="book-item_title">${book.title}</h3>
      <p class="author">by ${book.author} &bull; ${book.published}</p>
      <p>${book.synopsis}</p>
      <a href="#" class="button">Details</a>
    </div>
  `;

    grid.appendChild(bookItem);
});
