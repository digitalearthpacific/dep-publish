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
              <sld:ColorMapEntry quantity="0.00" color="#FFFFFF" opacity="0.0"/>
              <sld:ColorMapEntry quantity="0.10" color="#aee3c0" opacity="1.0"/>
              <sld:ColorMapEntry quantity="10.0" color="#6dd3ad" opacity="1.0"/>
              <sld:ColorMapEntry quantity="20.0" color="#44bcad" opacity="1.0"/>
              <sld:ColorMapEntry quantity="30.0" color="#35a1ab" opacity="1.0"/>
              <sld:ColorMapEntry quantity="40.0" color="#3487a6" opacity="1.0"/>
              <sld:ColorMapEntry quantity="50.0" color="#366da0" opacity="1.0"/>
              <sld:ColorMapEntry quantity="60.0" color="#3d5296" opacity="1.0"/>
              <sld:ColorMapEntry quantity="70.0" color="#403974" opacity="1.0"/>
              <sld:ColorMapEntry quantity="80.0" color="#35264c" opacity="1.0"/>
              <sld:ColorMapEntry quantity="90.0" color="#231526" opacity="1.0"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
