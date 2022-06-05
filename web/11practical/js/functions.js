"use strict";

$(function () {
   $("div").css({
       "flex-direction": "column",
       "align-items": "left",
       "margin": "3px"
   });
});

$("button").css("margin", "5px");

function addItemJQ() {
    let content = prompt("Содержимое списка: ");
    $("#list").append($(`<li>${content}</li>`));
}

function removeItemJQ() {
    let listItem = $("ol#list li");
    let len = listItem.length;

    if (len < 1) {
        alert("Список пустой, нечего удалять");
    } else {
        listItem.eq(len - 1).remove();
    }
}

$("button#add").click(function () {
    addItemJQ();
});

$("button#remove").click(function () {
    removeItemJQ();
});
