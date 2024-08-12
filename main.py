from domain.frame import FrameType
from domain.section import Section
from service.fit import fit_model
from service.measure import measure
from service.movement import extract_movement_millimeters_on_section
from service.optical import extract_3d_points_on_section
from service.reconstruct import construct_3d_points_from_sections
from service.video import open_video, close_video, get_frame_count, get_frame_type

VIDEO_PATH = r"..."


def main():
    open_video(VIDEO_PATH)

    sections: list[Section] = []
    for i in range(get_frame_count()):
        frame_type = get_frame_type(i)
        if frame_type == FrameType.LASER_EXPOSED:
            points = extract_3d_points_on_section(i)
            movement = extract_movement_millimeters_on_section(i)
            section = Section(
                idx=i,
                points=points,
                movement=movement,
            )
            sections.append(section)

    points = construct_3d_points_from_sections(sections)
    result = fit_model(points)
    measurement_result = measure(result)
    print(measurement_result)

    close_video()


if __name__ == '__main__':
    main()
