$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  const $list = $('<ul id="list_movies"></ul>');

  data.results.forEach(function(movie) {
    const $li = $('<li></li>');
    $li.text(movie.title);
    $list.append($li);
  });

  $('body').append($list);
});
