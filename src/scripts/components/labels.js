import tagChoices from "../../constants/choices.js"
import Alpine from "alpinejs"
import Tagify from "@yaireo/tagify"

Alpine.data("tags_input", () => ({
    init() {
        new Tagify(this.$el, {
            whitelist: tagChoices,
            enforceWhitelist: true,
            dropdown: {
                maxItems: 30,
                classname: 'tags-look',
                enabled: 0,
                closeOnSelect: false
            }
        })
    },
}))
