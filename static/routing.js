$(document).ready(function () {
  $('#about-button').on('click', function () {
    window.location.href = '/about';
  });

  $('#training-button').on('click', function () {
    window.location.href = '/learning/1';
  });

  $('#begin-quizzes').on('click', function () {
    window.location.href = '/big_quiz/1';
  });

  $('#beginQuiz-button').on('click', function () {
    window.location.href = '/big_quiz/1';
  });  

  $('#redo-learning').on('click', function () {
    window.location.href = '/learning/1';
  });  

  $('.js-return-home').click(function () {
    window.location.href = '/';
  });

  $('.js-retake-quiz').click(function () {
    window.location.href = '/big_quiz/1';
  });

  $('.js-redo-learning').click(function () {
    window.location.href = '/learning/1';
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
    window.location.href = `/quiz/5`;
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
