<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0" xmlns:sld="http://www.opengis.net/sld">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>Virtual</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry quantity="-7" color="#f7fbff" label="-7"/>
              <sld:ColorMapEntry quantity="6.9100000000000001" color="#deebf7" label="7"/>
              <sld:ColorMapEntry quantity="20.82" color="#c6dbef" label="21"/>
              <sld:ColorMapEntry quantity="34.730000000000004" color="#9ecae1" label="35"/>
              <sld:ColorMapEntry quantity="48.640000000000001" color="#6baed6" label="49"/>
              <sld:ColorMapEntry quantity="62.549999999999997" color="#4292c6" label="63"/>
              <sld:ColorMapEntry quantity="76.460000000000008" color="#2171b5" label="76"/>
              <sld:ColorMapEntry quantity="89.299999999999997" color="#08519c" label="89"/>
              <sld:ColorMapEntry quantity="100" color="#08306b" label="100"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
