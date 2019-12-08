function AlbumViewModel() {
	var self = this;
	self.id = ko.observable(0);
	self.nombre = ko.observable('');
    self.artista_nombre = ko.observable('');


	self.url=path_principal+'/api/';
	self.listado=ko.observableArray([]);
	self.mensaje=ko.observable('');

   	self.filtro_album={
        dato:ko.observable(''),
        id:ko.observable(''),
    };

	self.consultar = function(pagina){
		if (pagina > 0){
			self.filtro_album.dato($('#txtBuscar').val());
			path = self.url+'album/?format=json';
            parameter = { dato: self.filtro_album.dato(),
                          page: pagina 
                        };
            RequestGet(function (datos, estado, mensage) {
                if (datos!=null && datos.length > 0) {

                    self.listado(datos); 
                    self.mensaje('');
                } else {
                    self.listado([]);
                    self.mensaje(mensajeNoFound);//mensaje not found se encuentra el el archivo call-back.js
                }
                cerrarLoading();
            }, path, parameter,undefined,false);
		}

	}
    self.consulta_enter = function (d,e) {
        if (e.which == 13) {
            self.filtro_album.dato($('#txtBuscar').val());
            self.consultar(1);
        }
        return true;
    }
}


var album = new AlbumViewModel();
ko.applyBindings(album);