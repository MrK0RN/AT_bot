! function() {
    function e() {
        browser.permissions.request({
            origins: ["<all_urls>", "*://*.google.com/recaptcha/*", "*://*.recaptcha.net/recaptcha/*"]
        })
    }
    document.getElementById("setup-button").addEventListener("click", e)
}();