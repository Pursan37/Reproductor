function AlbumViewModel() {
	var self = this;
	self.id = ko.observable(0);
	self.nombre = ko.observable('');
    self.artista_nombre = ko.observable('');


	self.url=path_principal+'/api/';
	self.listado=ko.observableArray([]);
	self.mensaje=ko.observable('');


  self.listado_artistas = ko.observableArray([]);

   	self.filtro_album={
        dato:ko.observable(''),
        id:ko.observable(''),
    };
    
    

    self.albumVO={
        id:ko.observable(0),
        nombre:ko.observable('').extend({ required: { message: ' Digite el nombre del album.' } }),
        artista_id:ko.observable('').extend({ required: { message: ' Selecione al artista.' } })

    };

  self.consultar_artistas = function(pagina){
    if (pagina > 0){
      //self.filtro_album.dato($('#txtBuscar').val());
      path = self.url+'artista/?format=json';
            parameter = {};
            RequestGet(function (datos, estado, mensage) {
                if (datos!=null && datos.length > 0) {
                    self.listado_artistas(datos); 
                } else {
                    self.listado_artistas([]);
                }
                cerrarLoading();
            }, path, parameter,undefined,false);
    }    
  }

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

    self.eliminarAlbum = function (idAlbum) {
   // alert('eliminando el id ' + idAlbum);
    var path =self.url+'album/'+idAlbum+'/';
             var parameter = {};
             RequestAnularOEliminar("Esta seguro que desea eliminar este album?", path, parameter, function () {                 
                 self.consultar(1);
             })
  }
}


var album = new AlbumViewModel();
ko.applyBindings(album);