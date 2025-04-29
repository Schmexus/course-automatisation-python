from project.utils.api import Google_maps_api


"""Создание изменения и удаления новой локации"""
class Test_create_place():

    def test_create_new_place(self):
        print('Method POST')
        result_post = Google_maps_api.create_new_place()
        assert result_post.status_code == 200
        assert result_post.json()["status"] == "OK"
        place_id = result_post.json().get('place_id')
        print('Method GET')
        result_get = Google_maps_api.get_place(place_id)




