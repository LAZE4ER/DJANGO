$(document).ready(() => {
    const csrfToken = getCookie("csrftoken");

    
    const updateEngagement = (url, data, onSuccess) => {
        $.ajax({
            url: url,
            method: "POST",
            data: {
                ...data, 
                csrfmiddlewaretoken: csrfToken,
            },
            success: onSuccess,
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("Помилка запиту:", textStatus, errorThrown);
            }
        });
    };

    
    $(".like-button, .dislike-button").click(function() {
        const postId = $(this).data("id");
        const url = $(this).data("url"); 

        updateEngagement(url, { post_id: postId }, (response) => {
            $(`#likes-count-${postId}`).text(response.likes);
            $(`#dislikes-count-${postId}`).text(response.dislikes);
        });
    });

   
    $(".add-comment").click(function() {
        const postId = $(this).data("post-id");
        const url = $(this).data("url"); 
        const inputField = $(`.comment-input[data-post-id="${postId}"]`);
        const text = inputField.val();

        if (!text.trim()) return;

        updateEngagement(url, { post_id: postId, text: text }, (response) => {
            const list = $(`#comments-list-${postId}`);
            
            
            const newComment = `
                <li class="list-group-item d-flex justify-content-between" id="comment-${response.id}">
                    ${response.text}
                    <button class="btn btn-sm btn-outline-danger delete-comment" 
                            data-id="${response.id}" 
                            data-url="/delete_comment/${response.id}/">Delete</button>
                </li>`;
            
            list.append(newComment);
            $(`#comments-count-${postId}`).text(response.new_count);
            inputField.val(""); 
        });
    });

    
    $(document).on("click", ".delete-comment", function() {
        const commentId = $(this).data("id");
        const url = $(this).data("url");
        const postId = $(this).closest("ul").attr("id").split("-").pop();

        updateEngagement(url, { comment_id: commentId }, (response) => {
            $(`#comment-${commentId}`).remove();
            $(`#comments-count-${postId}`).text(response.new_count);
        });
    });
});