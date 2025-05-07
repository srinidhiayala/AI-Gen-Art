$(document).ready(function () {
  $('#about-button').on('click', function () {
    window.location.href = '/about';
  });

  $('#training-button').on('click', function () {
    window.location.href = '/learning/1';
  });

  $('#beginQuiz-button').on('click', function () {
    window.location.href = '/big_quiz/1';
  });  

  $('#next-button').click(function () {
    const nextId = $(this).data('next-id');
    if (nextId && nextId !== "null"){
      window.location.href = `/quiz/${nextId.substring(1)}`;
    }
  });

  $('#back-button').click(function () {
    const backId = $(this).data('back-id');
    if (backId && backId !== "null") {
      window.location.href = `/quiz/${backId.substring(1)}`;
    }
  });
  $('#back-bq-button').click(function () {
    const backId = $(this).data('back-id');
    if (backId && backId !== "null") {
      window.location.href = `/quiz/${backId.substring(1)}`;
    }
  });
  $('#back-mod-button').click(function () {
    const backId = $(this).data('back-id');
    if (backId && backId !== "null") {
      window.location.href = `/learning/${backId}`;
    }
  });  
  $('#next-mod-button').click(function () {
    const nextId = $(this).data('next-id');
    
    if (nextId && nextId !== "null" && nextId !== "big_quiz") {
      window.location.href = `/learning/${nextId}`;
    } else if (nextId === "big_quiz") {
      window.location.href = `/begin_quiz`;
    }
  });
  
  $('#about-next-button').click(function () {
    window.location.href = `/learning/1`;
  });

});
